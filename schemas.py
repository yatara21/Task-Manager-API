from pydantic import BaseModel, field_validator, Field
from typing import Optional
from datetime import datetime, timezone
from models import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus] = TaskStatus.pending
    priority: Optional[TaskPriority] = TaskPriority.medium
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(None, max_length=100)

    @field_validator("title")
    def title_must_not_be_blank(cls, v):
        if not v or not v.strip():
            raise ValueError("Title cannot be empty or whitespace only.")
        return v.strip()

    @field_validator("due_date")
    def due_date_must_be_future(cls, v):
        if v is not None and v <= datetime.now(timezone.utc):
            raise ValueError("Due date must be in the future.")
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(None, max_length=100)

    @field_validator("title")
    def title_must_not_be_blank(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Title cannot be empty or whitespace only.")
        return v.strip() if v else v

    @field_validator("due_date")
    def due_date_must_be_future(cls, v):
        if v is not None and v <= datetime.now(timezone.utc):
            raise ValueError("Due date must be in the future.")
        return v

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: Optional[datetime]
    due_date: Optional[datetime]
    assigned_to: Optional[str]

    model_config = {
        "from_attributes": True
    } 