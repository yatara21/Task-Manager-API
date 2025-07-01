# Task Management API


A FastAPI-based Task Management API using SQLModel, Pydantic, and SQLite. This project demonstrates modern Python API development, containerization, and deployment to the cloud.

## 🚀 Live Demo

**Task Manager API is now live on Azure!**

🌐 **API Base URL:** [http://buguard-backend-task.westeurope.azurecontainer.io:8000](http://buguard-backend-task.westeurope.azurecontainer.io:8000)  
📚 **Interactive Docs:** [http://buguard-backend-task.westeurope.azurecontainer.io:8000/docs](http://buguard-backend-task.westeurope.azurecontainer.io:8000/docs)

> ⏰ **Note:** This URL will be accessible only for 48 hours for testing purposes and then will not be available.

Try it out by visiting the API documentation link above!

---

## Features
- CRUD operations for tasks (Create, Read, Update, Delete)
- Data validation and error handling (Pydantic)
- Filtering and pagination
- Automatic API documentation (Swagger/OpenAPI)
- SQLite database (file-based, easy to use)
- Dockerized for easy deployment
- Ready for cloud deployment (e.g., Azure)

---

## Requirements
- Python 3.9+
- FastAPI
- uvicorn
- sqlmodel
- pydantic
- (For Docker) Docker Engine installed

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yatara21/Task-Manager-API.git
cd Task-Manager-API
```

---

### 2. Run Locally (Without Docker)

#### a. Install Python dependencies
```bash
pip install -r requirements.txt
```

#### b. Start the Application
```bash
python main.py
# Or (recommended):
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### c. Access the API
- Open [http://localhost:8000](http://localhost:8000)
- Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 3. Run with Docker

#### a. Build the Docker Image
```bash
docker build -t task-manager-api .
```

#### b. Run the Docker Container
```bash
docker run -d -p 8000:8000 --name task-manager-api task-manager-api
```

- The app will be available at [http://localhost:8000](http://localhost:8000)
- Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)



---

### 4. Deploy to Azure Cloud

#### Prerequisites
Make sure you have the following installed:
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Docker](https://docs.docker.com/get-docker/)
- Git

#### Step-by-Step Deployment

**Step 1: Login to Azure**
```bash
az login
```

**Step 2: Build Docker Image**
```bash
docker build -t task-mgr-api .
```

**Step 3: Create Resource Group**
```bash
az group create --name task-manager-rg --location westeurope
```

**Step 4: Deploy to Azure Container Instances**
```bash
az container create \
    --resource-group task-manager-rg \
    --name task-manager-api \
    --image task-mgr-api:latest \
    --os-type Linux \
    --cpu 1 \
    --memory 1.5 \
    --port 8000 \
    --dns-name-label task-manager-api-$(date +%s) \
    
```

**Step 5: Get Deployment Information**
```bash
az container show --resource-group task-manager-rg --name task-manager-api --query "ipAddress.fqdn" --output tsv
```


**Available Endpoints:**
- `GET /` - API information
- `GET /health` - Health check
- `GET /tasks` - Get all tasks (with filtering and pagination)
- `POST /tasks` - Create a new task
- `GET /tasks/{task_id}` - Get a specific task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task
- `GET /tasks/status/{status}` - Get tasks by status
- `GET /tasks/priority/{priority}` - Get tasks by priority

---

## API Usage

### Create a Task
```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'
```

### Get All Tasks (with optional filtering and pagination)
```bash
curl "http://localhost:8000/tasks?skip=0&limit=5&status=pending&priority=high"
```

### Get a Specific Task by ID
```bash
curl "http://localhost:8000/tasks/1"
```

### Update a Task
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
     -H "Content-Type: application/json" \
     -d '{"status": "completed", "priority": "urgent"}'
```

### Delete a Task
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

### Get Tasks by Status
```bash
curl "http://localhost:8000/tasks/status/completed"
```

### Get Tasks by Priority
```bash
curl "http://localhost:8000/tasks/priority/urgent"
```

See Swagger UI for full details and try out endpoints interactively.

---

## Project Structure
- `main.py` - FastAPI app and entry point
- `models.py` - SQLModel models and enums
- `schemas.py` - Pydantic schemas for validation
- `database.py` - Database session and initialization
- `routes.py` - All API endpoints
- `requirements.txt` - Python dependencies


---



#### Container Registry Authentication
If using Azure Container Registry, include registry credentials:
```bash
az container create \
    --resource-group my-rg \
    --name my-container \
    --image myacr.azurecr.io/my-image \
    --os-type Linux \
    --registry-login-server myacr.azurecr.io \
    --registry-username myusername \
    --registry-password mypassword
```
> **Note:** Make sure to replace `myacr.azurecr.io`, `myusername`, and `mypassword` with your actual Azure Container Registry credentials.


---

## Credits & Disclaimer | Very Important!!

This repository was developed as part of a comprehensive backend assessment, showcasing modern API development practices and cloud deployment capabilities. As this was my first experience working with the FastAPI framework, I strategically leveraged multiple learning resources to accelerate development while ensuring code quality and best practices.

**Learning Resources:**
- [FastAPI Tutorial Playlist](https://www.youtube.com/playlist?list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY) - Comprehensive video tutorials for framework fundamentals
- Official FastAPI, SQLModel, and Pydantic documentation for accurate implementation
- AI-assisted coding through Cursor AI editor for rapid development and code suggestions

**Containerization & Deployment:**
- The project includes a Dockerized setup for easy deployment and has been successfully deployed to Azure Cloud.

**Development Approach:**
Given the short deadline, I focused on understanding the core requirements, project structure, and database communication patterns rather than writing code from scratch. My approach prioritized:
- Thorough requirement analysis and architecture planning
- Understanding how different modules interact and communicate
- Leveraging existing documentation and tutorials for proven solutions
- Using AI assistance to accelerate implementation while maintaining code quality

This project demonstrates my ability to quickly adapt to new technology stacks and frameworks. I can efficiently familiarize myself with different tech stacks as project requirements demand, leveraging my DevOps background and rapid learning capabilities to deliver production-ready solutions regardless of the specific frameworks or languages involved.
