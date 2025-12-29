from sqlalchemy.orm import Session
from app.adapters.woocommerce_client import WooCommerceClient
from app.domain.models import Produto
from app.core.logger import logger

def sincronizar_produtos(db: Session) -> dict:
    """
    Sincroniza produtos do banco de dados para o WooCommerce.
    Retorna um dicionário com estatísticas da sincronização.
    """
    wc = WooCommerceClient()
    produtos = db.query(Produto).all()
    
    stats = {
        "total": len(produtos),
        "criados": 0,
        "atualizados": 0,
        "erros": 0
    }

    if not produtos:
        logger.warning("Nenhum produto encontrado no banco de dados.")
        return stats

    try:
        for p in produtos:
            try:
                data = {
                    "name": p.nome,
                    "regular_price": str(p.preco) if p.preco else "0",
                    "stock_quantity": p.estoque if p.estoque else 0,
                    "description": p.descricao or ""
                }

                if p.wc_id:
                    resultado = wc.update_product(p.wc_id, data)
                    if resultado:
                        stats["atualizados"] += 1
                        logger.info(f"Produto atualizado no WooCommerce: {p.nome} (ID: {p.wc_id})")
                    else:
                        stats["erros"] += 1
                        logger.warning(f"Falha ao atualizar produto {p.nome} no WooCommerce")
                else:
                    resultado = wc.create_product(data)
                    if resultado and "id" in resultado:
                        p.wc_id = resultado["id"]
                        stats["criados"] += 1
                        logger.info(f"Produto criado no WooCommerce: {p.nome} (ID: {resultado['id']})")
                    else:
                        stats["erros"] += 1
                        logger.warning(f"Falha ao criar produto {p.nome} no WooCommerce")

            except Exception as e:
                stats["erros"] += 1
                logger.error(f"Erro ao processar produto {p.nome}: {e}")

        db.commit()
        logger.info(f"Sincronização de produtos concluída: {stats['criados']} criados, {stats['atualizados']} atualizados")
    except Exception as e:
        db.rollback()
        logger.error(f"Erro ao sincronizar produtos: {e}", exc_info=True)
        raise

    return stats

