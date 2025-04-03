from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
import settings

MONGO_URI = "mongodb+srv://pixelo:skibidi123@cluster0.cturj0k.mongodb.net/"  # Zmień na swój URI, np. jeśli używasz MongoDB Atlas
DB_NAME = "blog_api"

client = MongoClient(uri = "mongodb+srv://pixelo:skibidi123@cluster0.cturj0k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", server_api=ServerApi('1'))
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
collection = database["users"]  # Przykładowa kolekcja
client = MongoClient(settings.mongodb_uri, settings.port)
db = client[customerdata]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    from fastapi import FastAPI
