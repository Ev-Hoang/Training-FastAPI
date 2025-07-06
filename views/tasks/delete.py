from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user
from models import TaskResponse

from testdb import Task, FakeUser

router = APIRouter()

@router.delete('/{task_id}', response_model = Task)
def delete_task(task_id: int, user: FakeUser = Depends(get_current_user)):
    for index, task in enumerate(user.tasks):
        if task.task_id == task_id:
            deleted_task = user.tasks.pop(index)
            return TaskResponse(message="Task deleted successfully", task_id=task_id)
    raise HTTPException(404, detail='task not found')