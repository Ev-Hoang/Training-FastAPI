from datetime import datetime
from typing import List
import os

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form

from auth import get_current_user
from models import TaskCreate, Progress, TaskResponse

from testdb import Task, FakeUser

router = APIRouter()

@router.post('/upload', response_model=Task)
async def upload_file(
    task_id: int = Form(...),
    file: UploadFile = File(...),
    user: FakeUser = Depends(get_current_user)
):
    task = next((t for t in user.tasks if t.task_id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    try:
        task_dir = f"descriptions/task_{task_id}"
        os.makedirs(task_dir, exist_ok=True)
        file_path = os.path.join(task_dir, file.filename)

        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)

        task.file_name = file.filename
        return TaskResponse(message="Task file upload successfully", task_id=task_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File saving failed: {str(e)}")


@router.post('', response_model=TaskResponse)
def create_task(task: TaskCreate, user: FakeUser = Depends(get_current_user)):
    new_task_id = max(t.task_id for t in user.tasks) + 1 if user.tasks else 1

    new_task = Task(
        task_id=new_task_id,
        task_name=task.task_name,
        task_description=task.task_description,
        priority=task.priority,
        progress=Progress.N,
        task_date=datetime.now().replace(microsecond=0),
        task_filename=""
    )
    user.tasks.append(new_task)
    return TaskResponse(message="Task created successfully", task_id=new_task_id)

@router.post("/bulk", response_model=List[Task])
def create_tasks_bulk(tasks: List[TaskCreate], user: FakeUser = Depends(get_current_user)):
    new_tasks = []
    new_task_id = max(task.task_id for task in user.tasks) + 1

    for i, task in enumerate(tasks):
        new_task = Task(task_id = new_task_id + i,
                    task_name = task.task_name,
                    task_description = task.task_description,
                    priority = task.priority,
                    progress= Progress.N,
                    task_date=datetime.now().replace(microsecond=0))
        user.tasks.append(new_task)
        new_tasks.append(new_task)
    return new_tasks