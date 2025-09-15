"""
Тесты для модуля widget.
"""

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card_card(input_str, expected):
    """Параметризованный тест маскировки карты."""
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_account(input_str, expected):
    """Параметризованный тест маскировки счёта."""
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "date_input, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ],
)
def test_get_date_valid(date_input, expected):
    """Тест корректного преобразования даты."""
    assert get_date(date_input) == expected


def test_get_date_invalid_format():
    """Тест ошибки при неверном формате даты."""
    with pytest.raises(ValueError):
        get_date("invalid-date")
