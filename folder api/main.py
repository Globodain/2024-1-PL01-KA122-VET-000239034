from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

app = FastAPI()

# Połączenie z MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.mojadb  # Zastąp 'mojadb' nazwą swojej bazy danych

@app.on_event("startup")
async def startup_db():
    print("Połączono z MongoDB")

@app.on_event("shutdown")
async def shutdown_db():
    client.close()
    print("Zamknięto połączenie z MongoDB")
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
from fastapi import HTTPException
from typing import List

# Dodawanie przedmiotu
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_dict = item.dict()
    result = await db.items.insert_one(item_dict)
    item.id = str(result.inserted_id)
    return item

# Pobieranie wszystkich przedmiotów
@app.get("/items/", response_model=List[Item])
async def read_items():
    items = []
    cursor = db.items.find()
    async for item in cursor:
        item["id"] = str(item["_id"])
        items.append(item)
    return items

# Pobieranie pojedynczego przedmiotu
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    item = await db.items.find_one({"_id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item["id"] = str(item["_id"])
    return item
