from fastapi import APIRouter, Depends, HTTPException

from auth import get_current_user
from models import Priority

from typing import List
from testdb import Task, FakeUser, user_task_cache

router = APIRouter()


@router.get("/completed", response_model=List[Task])
def get_completed_tasks(user: FakeUser = Depends(get_current_user)):
    """
    Lấy danh sách các task đã hoàn thành của người dùng hiện tại.

    Params:
    - user (FakeUser): Người dùng đã xác thực.

    Returns:
    - List[Task]: Danh sách task có progress = 1.
    """
    try:
        return [task for task in user.tasks if task.progress == 1]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Task retrieve failed: {str(e)}")


@router.get("/pending", response_model=List[Task])
def get_pending_tasks(user: FakeUser = Depends(get_current_user)):
    """
    Lấy danh sách các task đang chờ (chưa hoàn thành) của người dùng hiện tại.

    Params:
    - user (FakeUser): Người dùng đã xác thực.

    Returns:
    - List[Task]: Danh sách task có progress = 0.
    """
    try:
        return [task for task in user.tasks if task.progress == 0]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Task retrieve failed: {str(e)}")


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, user: FakeUser = Depends(get_current_user)):
    """
    Trả về chi tiết task theo ID của người dùng hiện tại.

    Params:
    - task_id (int): ID của task cần lấy.
    - user (FakeUser): Người dùng đã xác thực (lấy từ API key).

    Returns:
    - Task: Đối tượng task nếu tìm thấy.

    Notes:
    - Kiểm tra cache trước khi duyệt danh sách task.
    - Nếu không tìm thấy, trả về lỗi 404.
    """
    try:
        api_key = user.api_key
        if api_key not in user_task_cache:
            user_task_cache[api_key] = {}
        if task_id in user_task_cache[api_key]:
            return user_task_cache[api_key][task_id]

        for task in user.tasks:
            if task.task_id == task_id:
                user_task_cache[api_key][task_id] = task
                return task
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Task retrieve failed: {str(e)}")


@router.get('', response_model=List[Task])
def get_tasks(first_n: int = None, user: FakeUser = Depends(get_current_user)):
    """
    Lấy danh sách tất cả task của người dùng hiện tại.

    Params:
    - first_n (int, optional): Số lượng task đầu tiên cần lấy (nếu có).
    - user (FakeUser): Người dùng đã xác thực.

    Returns:
    - List[Task]: Danh sách task tương ứng.

    Notes:
    - Nếu không truyền `first_n`, trả về toàn bộ task.
    """
    try:
        if first_n:
            return user.tasks[:first_n]
        else:
            return user.tasks
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Task retrieve failed: {str(e)}")


@router.get("/by-priority/{priority}", response_model=List[Task])
def get_tasks_by_priority(priority: Priority,
                          user: FakeUser = Depends(get_current_user)):
    """
    Lấy danh sách các task theo độ ưu tiên của người dùng hiện tại.

    Params:
    - priority (Priority): Mức độ ưu tiên (L, M, H).
    - user (FakeUser): Người dùng đã xác thực.

    Returns:
    - List[Task]: Danh sách task có độ ưu tiên tương ứng.
    """
    try:
        return [task for task in user.tasks if task.priority == priority]
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Task retrieve failed: {str(e)}")
