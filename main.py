from fastapi import FastAPI
from routes.api_router import api

app = FastAPI()

app.include_router(api)
