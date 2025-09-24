"""
Модуль для генерации и фильтрации данных о транзакциях.
"""

from typing import Any, Dict, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, возвращающий транзакции с заданной валютой.

    :param transactions: Список словарей с данными о транзакциях
    :param currency: Код валюты (например "USD")
    :return: Итератор, возвращающий транзакции с указанной валютой
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции.

    :param transactions: Список словарей с данными о транзакциях
    :return: Итератор, возвращающий строки-описания операций
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное число (от 1 до 9999999999999999)
    :param stop: Конечное число (не включительно)
    :return: Итератор, возвращающий отформатированные номера карт
    """
    for number in range(start, stop):
        # Форматируем число в строку длиной 16 с ведущими нулями
        card_str = f"{number:016d}"
        # Разбиваем на блоки по 4 цифры
        formatted = f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted
