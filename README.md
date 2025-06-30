# Task Management API

A FastAPI-based Task Management API for assessment, using SQLModel, Pydantic, and SQLite.

## Features
- CRUD operations for tasks (Create, Read, Update, Delete)
- Data validation and error handling (pydantic)
- Filtering and pagination
- Automatic API documentation

## Requirements
- Python 3.9+
- See `requirements.txt` for dependencies

## Setup Instructions

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

# Or with Uvicorn (recommended for production)
uvicorn main:app --reload
```

## Access API Documentation
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)


## Example API Call
```bash
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'
```

## Project Structure
- `main.py` - FastAPI app and entry point
- `models.py` - SQLModel models and enums
- `schemas.py` - Pydantic schemas for validation
- `database.py` - Database session and initialization
- `routes.py` - All API endpoints
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Testing Endpoints
1. Start the app as above.
2. Visit [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.
3. Use tools like curl, Postman to test endpoints.

---
