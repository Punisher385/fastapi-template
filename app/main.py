from fastapi import FastAPI

from app.api.product import router as product_router

app = FastAPI()

app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "FastAPI Template"}