from sqlalchemy.orm import Session
from app.adapters.database import SessionLocal

def get_db():
    """Dependency injection para obter sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

