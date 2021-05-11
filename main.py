from fastapi import FastAPI
import route_gender

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"message": "pong"}

app.include_router(route_gender.router)