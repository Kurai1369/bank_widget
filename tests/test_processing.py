"""
Тесты для модуля processing.
"""

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_operations):
    """Тест фильтрации по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize(
    "state, count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
    ],
)
def test_filter_by_state_parametrize(sample_operations, state, count):
    """Параметризованный тест фильтрации по разным состояниям."""
    result = filter_by_state(sample_operations, state)
    assert len(result) == count


def test_sort_by_date_descending(sample_operations):
    """Тест сортировки по убыванию."""
    result = sort_by_date(sample_operations, reverse=True)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_operations):
    """Тест сортировки по возрастанию."""
    result = sort_by_date(sample_operations, reverse=False)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates)


def test_sort_by_date_empty_list():
    """Тест сортировки пустого списка."""
    assert sort_by_date([]) == []
