from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user
from models import TaskUpdate, TaskResponse

from testdb import Task, FakeUser, user_task_cache

router = APIRouter()


@router.put('/{task_id}', response_model=Task)
def update_task(task_id: int, updated_task: TaskUpdate,
                user: FakeUser = Depends(get_current_user)):
    """
    Cập nhật thông tin task theo ID cho người dùng hiện tại.

    Params:
    - task_id (int): ID của task cần cập nhật.
    - updated_task (TaskUpdate): Dữ liệu mới cho task.
    - user (FakeUser): Người dùng đã xác thực.

    Returns:
    - TaskResponse: Thông báo thành công và ID task đã cập nhật.

    Notes:
    - Chỉ cập nhật các trường được truyền (không None).
    - Nếu task không tồn tại, trả về lỗi 404.
    - Cập nhật cache nếu có.
    """
    try:
        api_key = user.api_key
        for task in user.tasks:
            if task.task_id == task_id:
                if updated_task.task_name is not None:
                    task.task_name = updated_task.task_name
                if updated_task.task_description is not None:
                    task.task_description = updated_task.task_description
                if updated_task.priority is not None:
                    task.priority = updated_task.priority
                if updated_task.progress is not None:
                    task.progress = updated_task.progress

                if api_key in user_task_cache:
                    user_task_cache[api_key][task_id] = task
                return TaskResponse(message="Task updated successfully",
                                    task_id=task_id)
        raise HTTPException(404, detail='task not found')
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Task update failed: {str(e)}")
