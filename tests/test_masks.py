"""
Тесты для модуля masks.
"""
import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_valid():
    """Тест корректной маскировки номера карты."""
    result = get_mask_card_number(7000792289606361)
    assert result == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_length():
    """Тест ошибки при неверной длине номера карты."""
    with pytest.raises(ValueError):
        get_mask_card_number(12345)


def test_get_mask_account_valid():
    """Тест корректной маскировки номера счёта."""
    result = get_mask_account(73654108430135874305)
    assert result == "**4305"


def test_get_mask_account_short():
    """Тест ошибки при слишком коротком номере счёта."""
    with pytest.raises(ValueError):
        get_mask_account(123)
