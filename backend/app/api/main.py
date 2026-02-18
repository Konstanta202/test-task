from fastapi import FastAPI
from app.api.routers.user import router as user_router


app = FastAPI()
app.include_router(user_router)


@app.get("/")
async def start():
    return {"Message": "backend work"}
