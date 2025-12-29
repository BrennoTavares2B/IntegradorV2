from sqlalchemy.orm import Session
from app.adapters.woocommerce_client import WooCommerceClient
from app.domain.models import Pedido
from app.core.logger import logger

def sincronizar_pedidos(db: Session) -> dict:
    """
    Sincroniza pedidos do WooCommerce para o banco de dados.
    Retorna um dicionário com estatísticas da sincronização.
    """
    wc = WooCommerceClient()
    pedidos = wc.get_orders()
    
    stats = {
        "total": 0,
        "novos": 0,
        "erros": 0
    }

    if not pedidos:
        logger.warning("Nenhum pedido retornado do WooCommerce.")
        return stats

    stats["total"] = len(pedidos)

    try:
        for p in pedidos:
            try:
                # Verifica se o pedido já existe
                if db.query(Pedido).filter(Pedido.order_id == p["id"]).first():
                    continue

                # Cria novo pedido
                novo = Pedido(
                    order_id=p["id"],
                    cliente=p.get("billing", {}).get("first_name", "") if p.get("billing") else "",
                    produtos=p.get("line_items", []),
                    total=float(p.get("total", 0)),
                    status=p.get("status", "")
                )
                db.add(novo)
                stats["novos"] += 1
                logger.info(f"Pedido salvo: {p['id']}")
            except Exception as e:
                stats["erros"] += 1
                logger.error(f"Erro ao processar pedido {p.get('id', 'desconhecido')}: {e}")

        db.commit()
        logger.info(f"Sincronização de pedidos concluída: {stats['novos']} novos pedidos")
    except Exception as e:
        db.rollback()
        logger.error(f"Erro ao sincronizar pedidos: {e}", exc_info=True)
        raise

    return stats

