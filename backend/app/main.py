from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="SICUYO Tickets API",
    description="Sistema de Gestión de Tickets",
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Bienvenido a SICUYO Tickets API"
    }
