from fastapi import FastAPI, Query,Body
from pydantic import BaseModel, HttpUrl
from starlette.requests import Request
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
class Item(BaseModel):
    name: HttpUrl
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


@app.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)