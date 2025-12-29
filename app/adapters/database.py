from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(settings.DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db() -> None:
    """Inicializa o banco de dados, criando todas as tabelas"""
    # Import aqui para evitar importação circular
    from app.domain.models import Pedido, Produto
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise Exception(f"Erro ao inicializar banco de dados: {e}") from e

