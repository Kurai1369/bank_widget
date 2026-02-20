"""
Модуль для загрузки данных из CSV и Excel.
"""

from typing import Any, Dict, List, cast

import pandas as pd


def load_transactions_from_csv(file_path: str) -> List[Dict[Any, Any]]:
    """
    Загружает транзакции из CSV-файла.

    :param file_path: Путь к CSV-файлу
    :return: Список словарей с транзакциями
    """
    df = pd.read_csv(file_path)
    return cast(List[Dict[Any, Any]], df.to_dict(orient="records"))


def load_transactions_from_excel(file_path: str) -> List[Dict[Any, Any]]:
    """
    Загружает транзакции из Excel-файла (.xlsx).

    :param file_path: Путь к Excel-файлу
    :return: Список словарей с транзакциями
    """
    df = pd.read_excel(file_path)
    return cast(List[Dict[Any, Any]], df.to_dict(orient="records"))
