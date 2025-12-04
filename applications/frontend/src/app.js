async function loadProducts(category = "") {
    const container = document.getElementById("products");
    container.innerHTML = "Loading...";

    let url = "/api/v1/products";
    if (category) {
        url += `?category=${encodeURIComponent(category)}`;
    }

    const response = await fetch(url);
    const products = await response.json();

    container.innerHTML = "";

    if (!products.length) {
        container.innerHTML = "<p>No products found.</p>";
        return;
    }

    products.forEach(p => {
        const item = document.createElement("div");
        item.className = "product";
        item.innerHTML = `
            <h3>${p.name}</h3>
            <p>Category: ${p.category}</p>
            <p>$${p.price.toFixed(2)}</p>
            <button onclick="addToCart('${p.id}')">Add to Cart</button>
        `;
        container.appendChild(item);
    });
}

async function addToCart(productId) {
    await fetch("/api/v1/cart/items", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ product_id: productId, quantity: 1 })
    });
    alert("Added to cart!");
}

// Initial load: show all
document.addEventListener("DOMContentLoaded", () => loadProducts());

