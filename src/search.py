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
    print(f"[DEBUG] Descriptions: {descriptions}")
    counter: Counter[str] = Counter()
    for i, desc in enumerate(descriptions):
        for j, cat in enumerate(categories):
            desc_lower = desc.lower()
            cat_lower = cat.lower()
            print(f"  [DEBUG] Desc[{i}] repr: {repr(desc_lower)}, Cat[{j}] repr: {repr(cat_lower)}")
            # Показать символы по ord()
            print(f"    [DEBUG] Desc chars: {[ord(c) for c in desc_lower]}")
            print(f"    [DEBUG] Cat chars: {[ord(c) for c in cat_lower]}")
            match = cat_lower in desc_lower
            print(f"    [DEBUG] Match: {match}")
            if match:
                print(f"    [DEBUG] Matched! Incrementing counter['{cat}']")
                counter[cat] += 1
    print(f"[DEBUG] Final Counter: {counter}")
    result = {cat: counter.get(cat, 0) for cat in categories}
    print(f"[DEBUG] Final Result: {result}")
    return result
