from typing import Dict


class Boto3ClientMock:
    def __init__(self, _, **kwargs) -> None:
        self.mock_data = kwargs["mock_data"]

    def put_item(self, **kwargs) -> Dict:
        data = self.mock_data["put_item"]
        if data.get("raise_exception"):
            raise "Mock AWS Exception"
        return data.get("response", {})
