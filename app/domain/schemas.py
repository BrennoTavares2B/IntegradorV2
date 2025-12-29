from pydantic import BaseModel
from typing import Optional

class PedidoSchema(BaseModel):
    order_id: int
    cliente: str
    total: float
    status: str

    class Config:
        from_attributes = True

class ProdutoSchema(BaseModel):
    nome: str
    preco: float
    estoque: int
    wc_id: Optional[int] = None

    class Config:
        from_attributes = True

