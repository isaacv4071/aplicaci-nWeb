from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.register import register_tortoise
from database.config import TORTOISE_ORM
from tortoise import Tortoise

app = FastAPI()


# enable schemas to read relationship between models
Tortoise.init_models(["database.models"], "models")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NEW
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello, World!"