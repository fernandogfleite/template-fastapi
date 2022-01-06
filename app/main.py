from fastapi import FastAPI

from app.db import (
    engine,
    Base,
    database
)


Base.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def index():
    return {"message": "Hello World"}
