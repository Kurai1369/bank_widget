"""
Модуль для обработки данных банковских операций.
"""

from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций, оставляя только те, у которых ключ 'state' соответствует заданному значению.

    Args:
        operations: Список словарей с данными операций.
        state: Значение для фильтрации по ключу 'state'. По умолчанию 'EXECUTED'.

    Returns:
        List: Новый список словарей, прошедших фильтрацию.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с данными операций.
        reverse: Порядок сортировки.
                True - по убыванию (сначала новые),
                False - по возрастанию (сначала старые).
                По умолчанию True.

    Returns:
        List: Новый список словарей, отсортированный по дате.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
