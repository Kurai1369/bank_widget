"""
Тесты для utils.
"""

import json
import tempfile

from src.utils import load_transactions_from_json


def test_load_transactions_valid_file():
    """Тест загрузки реального файла operations.json."""
    transactions = load_transactions_from_json("data/operations.json")
    assert len(transactions) > 0
    assert isinstance(transactions, list)
    assert "id" in transactions[0]


def test_load_transactions_valid():
    """Тест загрузки корректного JSON."""
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
        json.dump([{"id": 1}], f)
        temp_path = f.name

    result = load_transactions_from_json(temp_path)
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_load_transactions_empty_list():
    """Тест пустого списка."""
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
        json.dump([], f)
        temp_path = f.name

    result = load_transactions_from_json(temp_path)
    assert result == []


def test_load_transactions_not_list():
    """Тест, если JSON — не список."""
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
        json.dump({"key": "value"}, f)
        temp_path = f.name

    result = load_transactions_from_json(temp_path)
    assert result == []


def test_load_transactions_file_not_found():
    """Тест отсутствующего файла."""
    result = load_transactions_from_json("nonexistent.json")
    assert result == []
