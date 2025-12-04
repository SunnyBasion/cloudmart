# Submission.md  
**Student Name:** Sunny Basion
**Student ID:** 107827172  
**Course Code:** CSP451NIA  
**Project:** CSP451 Milestone 3: Enterprise Cloud Solution

---

## Project Overview
The CloudMart application is a containerized full-stack deployment running on
Azure Container Instances (ACI) and integrated into a continuous
deployment pipeline using GitHub Actions and Docker Hub.

Originally troubleshooting CORS issues between frontend and backend,
the solution shifted to using an **NGINX reverse proxy**, simplifying communication
and improving stability.

---

## Architecture Summary

| Component | Technology |
|----------|------------|
| Frontend | Vue.js running inside Docker |
| Backend API | Node.js (REST, `/api/v1/products`) |
| Reverse Proxy | NGINX |
| CI/CD | GitHub Actions → Docker Hub → Azure |
| Region | Canada East |
| Resource Group | Student-RG-1879876 |

---
## GitHub Repository Evidence

### Source Code Pushed & Private Visibility
> Repo URL: *[insert private GitHub link]*  
> Instructor added as collaborator

*Screenshot Placeholder — Repo main page & folders*  

### Secrets Configured
- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN
- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_TENANT_ID

*Screenshot Placeholder — GitHub secrets list (names only)*  

### Commit History
> Project contains multiple meaningful commits including Dockerfile and workflow updates

*Screenshot Placeholder — commit list view*

---

##  CI/CD Pipeline

GitHub workflow: `.github/workflows/deploy.yml`

Automations performed:
- Build backend + frontend Docker images
- Push tagged images to **Docker Hub**
- Deploy to **Azure Container Instances**
- Validate successful run (green build)

*Screenshot Placeholder — Actions run success*

---

## Azure Deployment Validation

### Resource Group View — Running Services
*Screenshot Placeholder — RG overview*

### Container Instances Running + Public URLs
Frontend:
> `http://cloudmart-frontend-10.canadaeast.azurecontainer.io/`

Backend API:
> `http://cloudmart-backend-10.canadaeast.azurecontainer.io/api/v1/products`

*Screenshot Placeholder — container details view*

---

## Cosmos DB (from design requirement)
> Database deployed using Azure Cosmos DB with product test data  
> Data Explorer shows proper containers

*Screenshot Placeholder — Data Explorer*

---

##  Network Security Group Evidence
> NSG configured to allow HTTP traffic

*Screenshot Placeholder — NSG screenshot*

---

## API Endpoint Testing

**Browser verification**  
> Products returned successfully in JSON

 *Screenshot Placeholder — API JSON screenshot*

**Curl example (to add later)**

```bash
curl http://cloudmart-backend-10.canadaeast.azurecontainer.io/api/v1/products
