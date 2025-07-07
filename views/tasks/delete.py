from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user
from models import TaskResponse

from testdb import Task, FakeUser

router = APIRouter()

@router.delete('/{task_id}', response_model = Task)
def delete_task(task_id: int, user: FakeUser = Depends(get_current_user)):
    """
    Xóa task theo ID cho người dùng hiện tại.

    Params:
    - task_id (int): ID của task cần xóa.
    - user (FakeUser): Người dùng đã xác thực.

    Returns:
    - TaskResponse: Thông báo xóa thành công và ID của task đã xóa.

    Notes:
    - Nếu không tìm thấy task, trả về lỗi 404.
    """
    try:
        for index, task in enumerate(user.tasks):
            if task.task_id == task_id:
                deleted_task = user.tasks.pop(index)
                return TaskResponse(message="Task deleted successfully", task_id=task_id)
        raise HTTPException(404, detail='task not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"task deleted failed: {str(e)}")