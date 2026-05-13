from fastapi import FastAPI

from app.api.product import router as product_router
from app.api.auth import router as auth_router

app = FastAPI()

app.include_router(product_router)
app.include_router(auth_router)