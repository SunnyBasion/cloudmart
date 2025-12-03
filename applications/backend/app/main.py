from fastapi import FastAPI, HTTPException
from .database import database, product_container
from .services.product_service import seed_products

app = FastAPI(title="CloudMart API", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Welcome to CloudMart!"}


@app.get("/health")
def health():
    """
    Simple health check that also reports Cosmos DB status.
    """
    try:
        # Try listing containers to confirm DB connectivity
        list(database.list_containers())
        db_status = "connected"
    except Exception:
        db_status = "unavailable"

    return {
        "status": "healthy",
        "service": "cloudmart-api",
        "database": "cosmos-db",
        "db_status": db_status,
    }


# -------------------------
# PRODUCT API ENDPOINTS
# -------------------------

@app.get("/api/v1/seed")
def seed():
    seed_products()
    return {"message": "Sample products seeded!"}


@app.get("/api/v1/products")
def get_products():
    items = list(product_container.query_items(
        query="SELECT * FROM c",
        enable_cross_partition_query=True
    ))
    return items

