from json import dumps, loads
from typing import Dict

from src.logger import logger
from src.product import Product


def main(event, context) -> Dict:

    logger.info(event)
    if "Records" in event.keys():
        event = loads(event["Records"][0]["body"])

    payload = event["payload"]

    product = Product()
    product.save_product(payload)

    return {
        "statusCode": 200,
        "body": dumps(
            {
                "payload": payload
            }
        ),
    }
