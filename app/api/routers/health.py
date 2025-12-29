from fastapi import APIRouter

router = APIRouter()

@router.get("")
@router.get("/")
def health_check():
    """Endpoint de health check"""
    return {"status": "ok", "service": "Integrador WooCommerce"}

