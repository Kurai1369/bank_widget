"""
Утилиты для работы с данными.
"""

import json
import logging
from typing import Dict, List

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
                logger.info(f"Загружено {len(data)} транзакций из {file_path}")
                return data
            else:
                logger.warning(f"Файл {file_path} содержит не список. Возвращён пустой список.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {file_path} содержит некорректный JSON.")
        return []
