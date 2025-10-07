from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=50, description="Title of the task")
    description: Optional[str] = Field(None, max_length=300, description="Detailed description of the task")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = Field(None, min_length=3, max_length=50, description="New title of the task")
    description: Optional[str] = Field(None, max_length=300, description="New detailed description of the task")
    status: Optional[str] = Field(None, description="Status of the task")

class TaskResponse(TaskBase):
    id: str = Field(..., description="Unique identifier of the task")
    status: str = Field("to do",  description="Status of the task")
    created_at: datetime = Field(..., description="Datetime when the task was created")

    class Config:
        from_attributes = True