from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    text:str = None
    is_done: bool = False

app = FastAPI()

items = []

@app.get("/")
async def root():
    return {"Hello" : "World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not Found")
    

