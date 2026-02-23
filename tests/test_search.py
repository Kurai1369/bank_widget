"""
Тесты для модуля search.
"""

import pytest

from src.search import count_transactions_by_category, search_transactions_by_description


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Открытие вклада", "amount": 200},
        {"description": "Перевод со счета на счет", "amount": 300},
        {"description": "Оплата покупки", "amount": 400},
    ]


def test_search_transactions_by_description(sample_transactions):
    """Тест поиска по описанию."""
    result = search_transactions_by_description(sample_transactions, "перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"


def test_count_transactions_by_category(sample_transactions):
    """Тест подсчёта по категориям."""
    categories = ["перевод", "вклад", "покупки"]
    result = count_transactions_by_category(sample_transactions, categories)
    print(result)
    assert result["перевод"] == 2
    assert result["вклад"] == 1
    assert result["покупки"] == 1
