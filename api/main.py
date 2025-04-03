from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os


load_dotenv()


app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")  
client = MongoClient(MONGO_URL)
db = client["jakub"]  
jakub_collection = db["users"]  


def serialize_document(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@app.get("/")
def home():
    return {"message": "FastAPI + MongoDB działa!"}


@app.get("/users")
def get_users():
    users = list(jakub_collection.find())
    return {"users": [serialize_document(user) for user in users]}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = jakub_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return serialize_document(user)
    return {"error": "User not found"}


@app.post("/users")
def add_user(user: dict):
    result = jakub_collection.insert_one(user)
    return {"message": "User added", "user_id": str(result.inserted_id)}



