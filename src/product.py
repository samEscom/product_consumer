from typing import Dict
from datetime import datetime

import requests

from src.constants import ECOMMERCE_API
from src.logger import logger
from src.aws import Aws


class Product:

    def __init__(self):
        self.aws = Aws()

    @staticmethod
    def save_product_ecommerce(token: str, sku: str, payload: Dict) -> bool:

        url = f"{ECOMMERCE_API}V1/products/{sku}"
        logger.info(f"url: {url}")
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.session().post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return True

        logger.info("Saved data from sku: %s", sku)

        return False

    def save_product(self, sku: str, data: Dict) -> bool:
        resume_data = {
            "Id": {
                "S": sku,
            },
            "date_send": {
                "S": str(datetime.now()),
            },
            "data": {
                "S": str(data),
            },
        }
        try:
            response = self.aws.save_data(resume_data)
            return response["ResponseMetadata"]["HTTPStatusCode"] == 200
        except Exception as e:
            logger.error(f"Cant replicate {sku}: {str(e)}")
            return False
