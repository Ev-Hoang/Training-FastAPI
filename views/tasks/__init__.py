from fastapi import APIRouter
from .create import router as create_router
from .read import router as read_router
from .update import router as update_router
from .delete import router as delete_router

router = APIRouter()
router.include_router(create_router, prefix="/tasks", tags=["Tasks : Create"])
router.include_router(read_router, prefix="/tasks", tags=["Tasks : Read"])
router.include_router(update_router, prefix="/tasks", tags=["Tasks : Update"])
router.include_router(delete_router, prefix="/tasks", tags=["Tasks : Delete"])
