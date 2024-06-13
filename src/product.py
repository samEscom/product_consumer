import requests
from typing import Dict
from src.logger import logger
from src.constants import ECOMMERCE_API


class Product:

    @staticmethod
    def save_product(token: str, sku: str, payload: Dict) -> bool:

        url = f"{ECOMMERCE_API}V1/products/{sku}"
        logger.info(f"url: {url}")
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.session().post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return True

        logger.info("Saved data from sku: %s", sku)

        return False
