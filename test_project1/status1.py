from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Set

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8001)