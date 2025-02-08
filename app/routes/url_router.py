from fastapi import APIRouter

url_router = APIRouter()
@url_router.get("/")
async def root():
    return {"message": "Hello World"}

@url_router.post("/create")
async def create():
    return {"message": "Hello World"}