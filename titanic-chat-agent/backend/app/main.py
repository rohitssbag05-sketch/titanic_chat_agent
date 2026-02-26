from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Titanic Chat Agent")
app.include_router(router)