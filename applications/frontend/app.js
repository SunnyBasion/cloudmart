const API_BASE = "http://cloudmart-backend.canadaeast.azurecontainer.io";

async function loadProducts() {
    const response = await fetch(`${API_BASE}/api/v1/products`);
    const products = await response.json();

    const container = document.getElementById("products");
    container.innerHTML = "";

    products.forEach(p => {
        const item = document.createElement("div");
        item.className = "product";
        item.innerHTML = `
            <h3>${p.name}</h3>
            <p>Category: ${p.category}</p>
            <p>$${p.price}</p>
            <button onclick="addToCart('${p.id}')">Add to Cart</button>
        `;
        container.appendChild(item);
    });
}

async function addToCart(productId) {
    await fetch(`${API_BASE}/api/v1/cart/items`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ product_id: productId, quantity: 1 })
    });
    alert("Added to cart!");
}

document.addEventListener("DOMContentLoaded", loadProducts);

