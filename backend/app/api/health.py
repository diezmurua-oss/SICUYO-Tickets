from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():
    return {
        "status": "ok",
        "application": "SICUYO Tickets",
        "version": "0.1.0",
    }
