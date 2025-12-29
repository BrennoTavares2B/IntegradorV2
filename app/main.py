from fastapi import FastAPI
from app.api.routers import health, pedidos, produtos
from app.adapters.database import init_db
from app.core.config import settings
from app.core.logger import logger

def create_app() -> FastAPI:
    """Factory function para criar a aplicação FastAPI"""
    app = FastAPI(
        title="Integrador WooCommerce",
        description="Sistema de sincronização WooCommerce ↔ Banco de Dados",
        version="1.0.0",
    )

    # Registra os routers
    app.include_router(health.router, prefix="/health", tags=["Status"])
    app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
    app.include_router(produtos.router, prefix="/produtos", tags=["Produtos"])

    @app.on_event("startup")
    async def startup_event():
        """Evento executado ao iniciar a aplicação"""
        try:
            settings.validate()
            init_db()
            logger.info("Aplicação iniciada com sucesso")
        except ValueError as e:
            logger.error(f"Erro de configuração: {e}")
        except Exception as e:
            logger.error(f"Erro ao inicializar banco de dados: {e}")

    return app

app = create_app()

