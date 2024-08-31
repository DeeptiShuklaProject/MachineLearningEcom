from fastapi import FastAPI
from api.endpoints import app as api_app

app = FastAPI()

app.include_router(api_app)
