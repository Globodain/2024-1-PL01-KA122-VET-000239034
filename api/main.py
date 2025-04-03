from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from api.database import collection

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    posts = await collection.find().to_list(100)
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})

@app.get("/posts/")
async def get_posts():
    posts = await collection.find().to_list(100)
    return posts

@app.post("/posts/")
async def create_post(post: dict):
    result = await collection.insert_one(post)
    return {"id": str(result.inserted_id)}