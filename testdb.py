from models import FakeUser, Task, Priority, Progress

from datetime import datetime

user_task_cache = {}

fake_users_db = {
    "abc123": FakeUser(
        api_key="abc123",
        tasks=[
            Task(
                task_id=1,
                task_name="Sports",
                task_description="Go play football",
                priority=Priority.M,
                progress=Progress.N,
                task_date=datetime.fromisoformat("2025-01-01T10:00:00")
            )
        ]
    ),
    "def456": FakeUser(
        api_key="def456",
        tasks=[
            Task(
                task_id=2,
                task_name="Sports",
                task_description="Go play football",
                priority=Priority.M,
                progress=Progress.N,
                task_date=datetime.fromisoformat("2025-01-01T10:00:00")
            ),
            Task(
                task_id=3,
                task_name="Sports",
                task_description="Go play football",
                priority=Priority.M,
                progress=Progress.N,
                task_date=datetime.fromisoformat("2025-01-01T10:00:00")
            )
        ]
    )
}
