from fastapi import FastAPI, Request

from app.auth.router import router as auth_router
from app.shop.router import router as shop_router
from app.user.router import router as user_router

app = FastAPI(
    title="Online Trading Site",
    description=("Online site for trading"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(auth_router)
app.include_router(shop_router)
app.include_router(user_router)
