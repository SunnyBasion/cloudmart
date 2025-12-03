from fastapi import FastAPI, HTTPException, Query, Body
from uuid import uuid4

from .database import (
    database,
    product_container,
    cart_container,
    orders_container
)

app = FastAPI(title="CloudMart API", version="1.0.0")


# -------------------------
# ROOT + HEALTH
# -------------------------

@app.get("/")
def root():
    return {"message": "Welcome to CloudMart!"}


@app.get("/health")
def health():
    try:
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

@app.get("/api/v1/products")
def get_products(category: str = Query(None)):
    if category:
        query = f"SELECT * FROM c WHERE c.category = '{category}'"
    else:
        query = "SELECT * FROM c"

    items = list(product_container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    return items


@app.get("/api/v1/products/{id}")
def get_product(id: str):
    query = f"SELECT * FROM c WHERE c.id = '{id}'"
    items = list(product_container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))

    if not items:
        raise HTTPException(status_code=404, detail="Product not found")

    return items[0]


@app.get("/api/v1/categories")
def list_categories():
    query = "SELECT DISTINCT c.category FROM c"
    items = list(product_container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    return sorted([item["category"] for item in items])


# -------------------------
# CART API ENDPOINTS
# -------------------------

USER_ID = "demo"  # Temporary since no login feature in assignment

@app.get("/api/v1/cart")
def get_cart():
    query = f"SELECT * FROM c WHERE c.user_id = '{USER_ID}'"
    items = list(cart_container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    return items


@app.post("/api/v1/cart/items")
def add_cart_item(product_id: str = Body(...), quantity: int = Body(1)):
    product_query = f"SELECT * FROM c WHERE c.id = '{product_id}'"
    product = list(product_container.query_items(
        query=product_query,
        enable_cross_partition_query=True
    ))

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    item = {
        "id": str(uuid4()),
        "user_id": USER_ID,
        "product_id": product_id,
        "quantity": quantity
    }

    cart_container.create_item(item)
    return item


@app.delete("/api/v1/cart/items/{id}")
def delete_cart_item(id: str):
    try:
        cart_container.delete_item(item=id, partition_key=USER_ID)
        return {"message": "Item removed"}
    except Exception:
        raise HTTPException(status_code=404, detail="Cart item not found")


# -------------------------
# ORDER API ENDPOINTS
# -------------------------

@app.post("/api/v1/orders")
def create_order():
    cart_items = get_cart()
    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    order = {
        "id": str(uuid4()),
        "user_id": USER_ID,
        "items": cart_items,
        "status": "confirmed"
    }

    orders_container.create_item(order)

    # Clear cart
    for item in cart_items:
        cart_container.delete_item(item=item["id"], partition_key=USER_ID)

    return order


@app.get("/api/v1/orders")
def get_orders():
    query = f"SELECT * FROM c WHERE c.user_id = '{USER_ID}'"
    items = list(orders_container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))
    return items

@app.delete("/api/v1/orders/{id}")
def delete_order(id: str):
    try:
        orders_container.delete_item(item=id, partition_key=USER_ID)
        return {"message": "Order deleted"}
    except Exception:
        raise HTTPException(status_code=404, detail="Order not found")

