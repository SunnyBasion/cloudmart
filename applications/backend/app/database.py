import os
from azure.cosmos import CosmosClient, PartitionKey

# Read connection info from environment variables
COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT", "")
COSMOS_KEY = os.getenv("COSMOS_KEY", "")

# Create Cosmos client
client = CosmosClient(COSMOS_ENDPOINT, credential=COSMOS_KEY)

# Database name (we already created this in Azure)
database_name = "cloudmart"
database = client.create_database_if_not_exists(id=database_name)

# Products container
product_container = database.create_container_if_not_exists(
    id="products",
    partition_key=PartitionKey(path="/category")
)

# Cart container
cart_container = database.create_container_if_not_exists(
    id="cart",
    partition_key=PartitionKey(path="/user_id")
)

# Orders container
orders_container = database.create_container_if_not_exists(
    id="orders",
    partition_key=PartitionKey(path="/user_id")
)

