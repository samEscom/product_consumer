from typing import Any, Dict

import boto3
from botocore.client import Config

from src.logger import logger
from src.constants import (
    AWS_REGION_EAST,
    AWS_SERVICE_DYNAMO,
    TABLE_NAME,
)


class Aws:
    @staticmethod
    def get_client(service: str):
        return boto3.client(
            service,
            region_name=AWS_REGION_EAST,
            config=Config(signature_version="s3v4"),
        )

    def save_data(self, summary: Dict) -> Any:
        try:
            dynamodb = self.get_client(AWS_SERVICE_DYNAMO)
            return dynamodb.put_item(TableName=TABLE_NAME, Item=summary)

        except Exception:
            raise
