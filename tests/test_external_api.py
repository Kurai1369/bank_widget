"""
Тесты для external_api.
"""

from unittest.mock import MagicMock, patch

import pytest
import requests

from src.external_api import convert_currency


@pytest.fixture
def sample_transaction_usd():
    return {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}


@patch("src.external_api.requests.get")
def test_convert_currency_usd_to_rub(mock_get, sample_transaction_usd):
    """Тест конвертации USD → RUB."""
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.5}}
    mock_get.return_value.raise_for_status = MagicMock()

    result = convert_currency(sample_transaction_usd)
    assert result == 100.0 * 90.5


@patch("src.external_api.requests.get")
def test_convert_currency_api_error(mock_get, sample_transaction_usd):
    """Тест при ошибке API."""
    mock_get.side_effect = requests.RequestException("Network error")
    result = convert_currency(sample_transaction_usd)
    assert result == 0.0


def test_convert_currency_rub_no_conversion():
    """Тест, если валюта уже RUB."""
    transaction = {"operationAmount": {"amount": "5000.0", "currency": {"code": "RUB"}}}
    result = convert_currency(transaction)
    assert result == 5000.0
