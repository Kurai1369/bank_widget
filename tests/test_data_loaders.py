"""
Тесты для модуля data_loaders.
"""

from unittest.mock import patch

import pytest

from src.data_loaders import load_transactions_from_csv, load_transactions_from_excel


@pytest.fixture
def sample_csv_content():
    return """id,state,date,operationAmount.amount,operationAmount.currency.code
1,EXECUTED,2024-01-01,100.0,USD
2,CANCELED,2024-01-02,200.0,RUB
"""


@patch("src.data_loaders.pd.read_csv")
def test_load_transactions_from_csv(mock_read_csv, sample_csv_content):
    """Тест загрузки из CSV с mock."""
    mock_df = pytest.importorskip("pandas").DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2024-01-01",
                "operationAmount.amount": "100.0",
                "operationAmount.currency.code": "USD",
            },
            {
                "id": 2,
                "state": "CANCELED",
                "date": "2024-01-02",
                "operationAmount.amount": "200.0",
                "operationAmount.currency.code": "RUB",
            },
        ]
    )
    mock_read_csv.return_value = mock_df

    result = load_transactions_from_csv("dummy.csv")
    assert len(result) == 2
    assert result[0]["id"] == 1


@patch("src.data_loaders.pd.read_excel")
def test_load_transactions_from_excel(mock_read_excel):
    """Тест загрузки из Excel с mock."""
    mock_df = pytest.importorskip("pandas").DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2024-01-01",
                "operationAmount.amount": "100.0",
                "operationAmount.currency.code": "USD",
            },
        ]
    )
    mock_read_excel.return_value = mock_df

    result = load_transactions_from_excel("dummy.xlsx")
    assert len(result) == 1
    assert result[0]["id"] == 1
