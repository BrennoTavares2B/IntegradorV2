from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.pedidos_service import sincronizar_pedidos
from app.core.logger import logger

router = APIRouter()

@router.post("/sincronizar")
def sync_pedidos(db: Session = Depends(get_db)):
    """
    Sincroniza pedidos do WooCommerce para o banco de dados
    """
    try:
        stats = sincronizar_pedidos(db)
        return {
            "detail": "Pedidos sincronizados com sucesso!",
            "stats": stats
        }
    except Exception as e:
        logger.error(f"Erro ao sincronizar pedidos: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erro ao sincronizar pedidos: {str(e)}")

