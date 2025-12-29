from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.produtos_service import sincronizar_produtos
from app.core.logger import logger

router = APIRouter()

@router.post("/sincronizar")
def sync_produtos(db: Session = Depends(get_db)):
    """
    Sincroniza produtos do banco de dados para o WooCommerce
    """
    try:
        stats = sincronizar_produtos(db)
        return {
            "detail": "Produtos sincronizados com sucesso!",
            "stats": stats
        }
    except Exception as e:
        logger.error(f"Erro ao sincronizar produtos: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Erro ao sincronizar produtos: {str(e)}")

