"""
Модуль для обработки данных банковских операций.
"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """
    Маскирует номер карты или счёта в зависимости от типа.

    :param card_or_account_info: Строка с типом и номером карты/счёта
    :return: Строка с замаскированным номером
    """
    # Разделяем строку на части (последние 16-20 цифр — это номер)
    parts = card_or_account_info.split()
    if not parts:
        raise ValueError("Неверный формат строки")

    # Номер — всегда последний индекс
    number_str = parts[-1]
    prefix = " ".join(parts[:-1])  # всё, кроме последнего

    if not number_str.isdigit():
        raise ValueError("Номер должен состоять только из цифр")

    number = int(number_str)

    # Определяем, счёт это или карта
    if prefix.startswith("Счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{prefix} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой из формата ISO-даты (стоки) в формат ДД.ММ.ГГГГ (объект даты).

    :param date_string: Строка с датой в формате ISO
    :return: Строка с датой в формате ДД.ММ.ГГГГ
    """
    from datetime import datetime # daytime встроенный модуль Python для работы с датами

    dt = datetime.fromisoformat(date_string) # превращает строку в объект даты
    return dt.strftime("%d.%m.%Y") # превращает объект даты обратно в строку
