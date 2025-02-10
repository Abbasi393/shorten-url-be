from fastapi import APIRouter

index_router = APIRouter()


@index_router.get("/")
async def root():
    return {"message": "Hello World"}
