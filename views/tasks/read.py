from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user
from models import Priority

from typing import List
from testdb import Task, FakeUser, user_task_cache

router = APIRouter()

@router.get("", response_model=List[Task])
def get_tasks(user: FakeUser = Depends(get_current_user)):
    return user.tasks

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, user: FakeUser = Depends(get_current_user)):
    """
    Des: Get detail task by id
    Arg: task_id (str) ...
    Returns:
        Object(task), List,....
    """
    # task_id khong ton tai
    try:
        api_key = user.api_key
        if api_key not in user_task_cache:
            user_task_cache[api_key] = {}
        if task_id in user_task_cache[api_key]:
            return user_task_cache[api_key][task_id]
        
        for task in user.tasks:
            if task.task_id == task_id:
                user_task_cache[api_key][task_id] = task
            
                return HTTPException(status_code=200, detail="Task not found", data=task)
            
                # return task -> khong dung cai format yeu de hien thi o client
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise e

@router.get('', response_model = List[Task])
def get_tasks(first_n: int = None, user: FakeUser = Depends(get_current_user)):
    if first_n:

        return user.tasks[:first_n]
    else:
        return user.tasks

@router.get("/completed", response_model=List[Task])
def get_completed_tasks(user: FakeUser = Depends(get_current_user)):
    return [task for task in user.tasks if task.progress == 1]

@router.get("/pending", response_model=List[Task])
def get_pending_tasks(user: FakeUser = Depends(get_current_user)):
    return [task for task in user.tasks if task.progress == 0]

@router.get("/by-priority/{priority}", response_model=List[Task])
def get_tasks_by_priority(priority: Priority, user: FakeUser = Depends(get_current_user)):
    return [task for task in user.tasks if task.priority == priority]