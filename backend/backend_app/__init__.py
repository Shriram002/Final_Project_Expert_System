from fastapi import FastAPI
from backend_app.routes import router

app = FastAPI()

app.include_router(router)
