""" import uvicorn """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from database.register import register_tortoise
from database.config import TORTOISE_ORM


# enable schemas to read relationship between models
Tortoise.init_models(["database.models"], "models")
from routes import users, owners, vehicles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(owners.router)
app.include_router(vehicles.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"

""" if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) """