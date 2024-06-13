from json import dumps, loads
from typing import Dict

from src.logger import logger
from src.product import Product


def main(event, context) -> Dict:

    logger.info(f"input event: {event}")
    if "Records" in event.keys():
        event = loads(event["Records"][0]["body"])

    sku = event.get("sku")
    product_save = event.get("product")
    token = event.get("token")
    is_saved = False

    product = Product()

    if event["update"]:
        is_saved = product.save_product(
            str(token),
            str(sku),
            product_save
        )

    return {
        "statusCode": 200,
        "body": dumps(
            {
                "sku": sku,
                "isSaved": is_saved,
            }
        ),
    }
