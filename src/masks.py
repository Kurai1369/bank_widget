"""
Модуль для маскировки номеров карт и счетов.
"""


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты (целое число)
    :return: Замаскированный номер карты
    """
    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен быть 16-значным числом")

    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счёта в формате **XXXX.

    :param account_number: Номер счёта (целое число)
    :return: Замаскированный номера счёта
    """
    account_str = str(account_number)
    if len(account_str) < 4 or not account_str.isdigit():
        raise ValueError("Номер счёта должен содержать минимум 4 цифры")

    return f"**{account_str[-4:]}"
