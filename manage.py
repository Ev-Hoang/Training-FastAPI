from fastapi import FastAPI

from views.tasks import router as task_router
from utils.middleware import log_requests

api = FastAPI()

api.middleware("http")(log_requests)
api.include_router(task_router)


@api.get("/")
def root():
    return {"message": "Hello, world"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("manage:api", host="0.0.0.0", port=8000, reload=True)
