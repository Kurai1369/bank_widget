"""
Утилиты для работы с данными.
"""

import json
from typing import Dict, List


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Загружает транзакции из JSON-файла.

    :param file_path: Путь к JSON-файлу
    :return: Список словарей с транзакциями или пустой список
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
