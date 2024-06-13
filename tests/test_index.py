import json
import requests
from index import handler

from .mocks.requests.requests import RequestMock

from src.constants import ECOMMERCE_API


def test_save_product(monkeypatch):
    def mock_requests_session():
        return RequestMock(
            mock_data={
                f"{ECOMMERCE_API}V1/products/123": {
                    "raise_exception": False,
                    "response": "12345678",
                    "status_code": 200,
                },
            }
        )

    monkeypatch.setattr(requests, "session", mock_requests_session)

    response = handler(
        event={"update": True, "token": "456", "sku": "123", "product": {"sku": "123", "price": "123.08"}},
        context=None,
    )

    assert response["statusCode"] == 200

    body = json.loads(response["body"])

    assert body["sku"] == "123"
    assert body["isSaved"] is True


def test_save_product_fail(monkeypatch):
    def mock_requests_session():
        return RequestMock(
            mock_data={
                f"{ECOMMERCE_API}V1/products/456": {
                    "raise_exception": False,
                    "response": "12345678",
                    "status_code": 500,
                },
            }
        )

    monkeypatch.setattr(requests, "session", mock_requests_session)

    response = handler(
        event={"update": True, "token": "fail", "sku": "456", "product": {"sku": "456", "price": "123.08"}},
        context=None,
    )

    assert response["statusCode"] == 200

    body = json.loads(response["body"])

    assert body["sku"] == "456"
    assert body["isSaved"] is False
