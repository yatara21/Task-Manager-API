# Task Management API

A FastAPI-based Task Management API for task tracking and management, using SQLModel, Pydantic, and SQLite. This project demonstrates modern Python API development, containerization, and deployment to the cloud.

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
- See `requirements.txt` for dependencies
- (For Docker) Docker Engine installed

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <REPO_URL>
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
# Or (recommended for production):
uvicorn main:app --host 0.0.0.0 --port 8000
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

#### c. Image Size Optimization
- Uses `python:3.11-alpine` for a minimal image (~115MB)
- `.dockerignore` excludes unnecessary files (docs, tests, configs, etc.)

---

### 4. Access via Azure Cloud (Deployed Version)
If you want to use the cloud-hosted version, simply visit:

```
<AZURE_CLOUD_URL>
```

- Replace `<AZURE_CLOUD_URL>` with the actual URL once available.
- Swagger docs: `<AZURE_CLOUD_URL>/docs`

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
- `README.md` - This file

---

## Troubleshooting
- **Port already in use:** Stop other services using port 8000 or change the port in the run command.
- **Database not persisting:** The SQLite file (`tasks.db`) is created in the container. For persistent data, mount a volume.
- **Docker build errors:** Ensure you have the latest Docker and a stable internet connection.
- **Azure deployment issues:** Check logs and ensure environment variables and ports are set correctly.

---

## Credits & Disclaimer

This project was created as a learning exercise to explore FastAPI, modern Python API development, and DevOps best practices. The implementation was guided by a YouTube tutorial and supported by the Cursor AI editor, as FastAPI is a new framework for me.

**Learning Resources:**
- [FastAPI Tutorial Playlist](https://www.youtube.com/playlist?list=PL-2EBeDYMIbTJrr9qaedn3K_5oe0l4krY)

**Containerization & Deployment:**
- The project includes a Dockerized setup for easy deployment and has been successfully deployed to Azure Cloud. The public URL will be provided as soon as it is available.

**Approach:**
- My focus was on understanding requirements, consulting official documentation, and designing a clean, maintainable architecture. I prioritized best practices in structure, validation, and deployment, even as I learned the FastAPI framework itself.

**Note:**
- This project demonstrates my ability to quickly learn and adapt to new technologies and tech stacks. My background in DevOps and cloud enables me to deliver robust solutions, even when working with unfamiliar frameworks or languages.
