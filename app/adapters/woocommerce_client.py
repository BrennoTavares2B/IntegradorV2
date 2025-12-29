import requests
from typing import Optional, Dict, Any, List
from app.core.config import settings
from app.core.logger import logger

class WooCommerceClient:
    def __init__(self):
        self.base = settings.WC_BASE_URL.rstrip('/')
        self.auth = (settings.WC_KEY, settings.WC_SECRET)

    def _request(self, method: str, endpoint: str, **kwargs) -> Optional[Any]:
        url = f"{self.base}/wp-json/wc/v3/{endpoint.lstrip('/')}"
        try:
            res = requests.request(method, url, auth=self.auth, timeout=10, **kwargs)
            res.raise_for_status()
            return res.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro API WooCommerce: {e} | endpoint={endpoint}")
            return None
        except Exception as e:
            logger.error(f"Erro inesperado na API WooCommerce: {e} | endpoint={endpoint}")
            return None

    def get_orders(self) -> Optional[List[Dict[str, Any]]]:
        """Busca todos os pedidos do WooCommerce"""
        return self._request("GET", "orders")

    def get_products(self) -> Optional[List[Dict[str, Any]]]:
        """Busca todos os produtos do WooCommerce"""
        return self._request("GET", "products")

    def create_product(self, data: dict) -> Optional[Dict[str, Any]]:
        """Cria um novo produto no WooCommerce"""
        return self._request("POST", "products", json=data)

    def update_product(self, wc_id: int, data: dict) -> Optional[Dict[str, Any]]:
        """Atualiza um produto existente no WooCommerce"""
        return self._request("PUT", f"products/{wc_id}", json=data)

