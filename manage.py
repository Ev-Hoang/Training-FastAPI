from fastapi import FastAPI

from views.tasks import router as task_router
from utils.middleware import log_requests

api = FastAPI()

api.middleware("http")(log_requests)
api.include_router(task_router)