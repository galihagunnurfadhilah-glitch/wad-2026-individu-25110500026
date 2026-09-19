from fastapi import FastAPI
from .routers.menu import router as menu_router

app = FastAPI()

app.include_router(menu_router)


@app.get("/health")
def health():
    return {"status": "ok"}