from ..database import product_container


def seed_products():
    sample_products = [
        {
            "id": "1",
            "name": "Laptop",
            "price": 999.99,
            "category": "electronics",
            "stock": 10
        },
        {
            "id": "2",
            "name": "Headphones",
            "price": 199.99,
            "category": "electronics",
            "stock": 20
        },
        {
            "id": "3",
            "name": "T-Shirt",
            "price": 24.99,
            "category": "clothing",
            "stock": 30
        }
    ]

    for product in sample_products:
        try:
            product_container.create_item(body=product)
        except Exception:
            # Ignore if item already exists
            pass

