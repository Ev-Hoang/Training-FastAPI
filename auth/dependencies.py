from fastapi import HTTPException, Header

from testdb import fake_users_db


def get_current_user(x_api_key: str = Header(...)):
    user = fake_users_db.get(x_api_key)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return user
