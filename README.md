# CloudMart – Cloud-Native Retail Web App

CloudMart is a fully-deployed, cloud-native web application designed to simulate an online retail shopping experience. It includes a public frontend UI, secure backend API, cloud database, and automated deployment pipeline.

## Architecture & Technologies Used
- **Azure Container Instances** for hosting both frontend and backend
- **Cosmos DB** for product, cart, and order storage
- **FastAPI** backend with RESTful API routes
- **NGINX** frontend serving static files + reverse proxy to backend
- **Docker** containerization for consistent deployment
- **GitHub Actions CI/CD** for automated build + deploy
- **Network Security Group rules** to control inbound traffic

## App Features
- Homepage displays product catalog retrieved from backend API
- Category filtering (Electronics / Clothing / All)
- Shopping cart with quantity tracking and item removal
- Order confirmation with backend persistence
- Health check endpoint for service monitoring

## Cloud Deploy Automation
Every push to the `main` branch triggers:
1. Docker image build for backend + frontend
2. Images pushed to Docker Hub
3. Automatic deployment to Azure Container Instances

This ensures fast, repeatable, and reliable deployments without manual intervention.

## Security
- Azure NSG configured to allow only HTTP/HTTPS/SSH
- Cosmos DB access secured using primary keys (no public exposure)
- Backend isolated behind NGINX proxy for controlled routing

---

This project demonstrates practical cloud deployment, container orchestration, secure networking configurations, and DevOps automation in a real-world architecture.
