"""
Модуль для поиска и подсчета транзакций.
"""

from collections import Counter
import re
from typing import Any, Dict, List


def search_transactions_by_description(transactions: List[Dict[Any, Any]], search: str) -> List[Dict[Any, Any]]:
    """
    Ищет транзакции, в описании которых встречается строка search.

    :param transactions: Список словарей с транзакциями
    :param search: Строка для поиска
    :return: Список транзакций, содержащих строку
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict[Any, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по заданным категориям (description).

    :param transactions: Список словарей с транзакциями
    :param categories: Список категорий
    :return: Словарь с количеством транзакций по категориям
    """
    descriptions = [t.get("description", "") for t in transactions]
    counter: Counter[str] = Counter()
    for desc in descriptions:
        for cat in categories:
            if cat.lower() in desc.lower():
                counter[cat] += 1
    return {cat: counter.get(cat, 0) for cat in categories}
