from enum import IntEnum
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Priority(IntEnum):
    L = 3
    M = 2
    H = 1


class Progress(IntEnum):
    N = 0
    Y = 1


class TaskResponse(BaseModel):
    message: str
    task_id: int


class TaskBase(BaseModel):
    task_name: str = Field(..., min_length=3,
                           max_length=512, description="Name")
    task_description: str = Field(..., description="description")
    priority: Priority = Field(default=Priority.L, description="Priority")
    file_name: str = Field(default="", description="File name")


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    task_id: int = Field(..., description="id")
    progress: Progress = Field(default=Progress.N, description="Progress")
    task_date: datetime = Field(..., description="Date")


class TaskUpdate(BaseModel):
    task_name: Optional[str] = Field(
        None, min_length=3, max_length=512, description="Name")
    task_description: Optional[str] = Field(None, description="description")
    priority: Optional[Priority] = Field(None, description="Priority")
    progress: Optional[Progress] = Field(None, description="Progress")


class FakeUser(BaseModel):
    api_key: str = Field(...)
    tasks: List[Task] = Field(default_factory=list)
