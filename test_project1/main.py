from fastapi import FastAPI, Query,Body, Cookie, status
from pydantic import BaseModel, HttpUrl, EmailStr
from starlette.requests import Request
from typing import List, Union
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
class Item(BaseModel):
    name: str
    description: str

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserInDB(BaseModel):
    username: str
    hashed_passwordss: str
    email: EmailStr
    full_name: str = None


def fake_password_hasher(raw_password):
    return "supersecret" + raw_password


def fake_save_user(user_in):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_passwordss=hashed_password)
    print("User saved! ..not really")
    return user_in_db

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}


@app.post("/user/", response_model=UserOut, status_code=status.HTTP_406_NOT_ACCEPTABLE )
async def create_user(*, user_in: UserIn):
    user_saved = fake_save_user(user_in)
    print(user_saved)
    return user_saved


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)