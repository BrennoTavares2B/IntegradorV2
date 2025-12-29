from sqlalchemy import Column, Integer, String, Float, JSON
from app.adapters.database import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, unique=True, nullable=False)
    cliente = Column(String)
    produtos = Column(JSON)
    total = Column(Float)
    status = Column(String)

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    wc_id = Column(Integer, unique=True, nullable=True)
    nome = Column(String, nullable=False)
    preco = Column(Float)
    estoque = Column(Integer)
    descricao = Column(String)

