import requests
from typing import Dict
from src.logger import logger
from src.constants import ECOMMERCE_API, ECOMMERCE_USER, ECOMMERCE_PASS


class Product:

    @staticmethod
    def save_product(sku: str, payload: Dict) -> bool:

        url = f"{ECOMMERCE_API}1/products/{sku}"
        data = {"username": ECOMMERCE_USER, "password": ECOMMERCE_PASS}
        response = requests.session().post(url, json=data)

        if response.status_code == 200:
            return True

        logger.info("Saved data: %s", payload["product"])

        return False

