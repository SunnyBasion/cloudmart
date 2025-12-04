# Submission.md  
**Student Name:** Sunny Basion
**Student ID:** 107827172  
**Course Code:** CSP451NIA  
**Project:** CloudMart – Azure CI/CD Deployment

---

## 📌 Project Overview
The CloudMart application is a containerized full-stack deployment running on
Azure Container Instances (ACI) and integrated into a continuous
deployment pipeline using GitHub Actions and Docker Hub.

Originally troubleshooting CORS issues between frontend and backend,
the solution shifted to using an **NGINX reverse proxy**, simplifying communication
and improving stability.

---

## 🏗 Architecture Summary

| Component | Technology |
|----------|------------|
| Frontend | Vue.js running inside Docker |
| Backend API | Node.js (REST, `/api/v1/products`) |
| Reverse Proxy | NGINX (CORS configuration removed after proxy deployment) |
| CI/CD | GitHub Actions → Docker Hub → Azure Container Instances |
| Region | Canada East |
| Resource Group | Student-RG-1879876 |

---

## 🧩 GitHub Repository Evidence

### Source Code Pushed & Private Visibility
> Repo URL: *[Insert GitHub private repo URL]*  
> Instructor added as collaborator

📸 **Repo Overview Screenshot**  
*(paste image link: `screenshots/github_repo_overview.png`)*

### Secrets Configured
Repository secrets added for automated deployment:
- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN
- COSMOS_KEY
- COSMOS_ENDPOINT
- AZURE_CREDENTIALS

📸 **Secrets Screenshot**  
*(paste image link: `screenshots/github_secrets.png`)*

### CI/CD Workflow Executions
> Continuous deployment triggered on push to `main`

📸 **GitHub Actions Success**  
*(paste image link: `screenshots/github_actions_success.png`)*

---

## ☁️ Azure Deployment Validation

### Resource Group Overview
📸 *(paste image: `screenshots/azure_rg_overview.png`)*

### Container Instances Running
Frontend URL:  
`http://cloudmart-frontend-canadaeast.azurecontainer.io/`

Backend API URL:  
`http://cloudmart-backend-canadaeast.azurecontainer.io/api/v1/products`

📸 *(paste image: `screenshots/azure_container_instances.png`)*

### Cosmos DB Verification
📸 *(paste image: `screenshots/cosmosdb_data_explorer.png`)*

### Network Security Rules
📸 *(paste image: `screenshots/azure_nsg_rules.png`)*

---

## 🔍 API Endpoint + App Testing

### 1️⃣ Homepage – Products Visible
📸 *(paste image: `screenshots/app_homepage.png`)*

### 2️⃣ Category Filtering Working
📸 *(paste image: `screenshots/app_category_filter.png`)*

### 3️⃣ Shopping Cart – Items + Total
📸 *(paste image: `screenshots/app_shopping_cart.png`)*

### 4️⃣ Order Confirmation Page
📸 *(paste image: `screenshots/app_order_confirmation.png`)*

### 5️⃣ Health Endpoint
📸 *(paste image: `screenshots/app_health_endpoint.png`)*

Curl example (optional to add):

```bash
curl http://cloudmart-backend-canadaeast
