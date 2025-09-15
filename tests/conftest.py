"""
Фикстуры для тестов.
"""

import pytest


@pytest.fixture
def sample_operations():
    """Пример списка операций."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def card_numbers():
    """Номера карт."""
    return [
        "Visa Platinum 7000792289606361",
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
    ]


@pytest.fixture
def account_numbers():
    """Номера счетов."""
    return [
        "Счет 64686473678894779589",
        "Счет 35383033474447895560",
        "Счет 73654108430135874305",
    ]
