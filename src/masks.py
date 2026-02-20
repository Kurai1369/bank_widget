"""
Модуль для маскировки номеров карт и счетов.
"""
import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты по формату XXXX XX** **** XXXX.

    :param card_number: Номер карты (целое число)
    :return: Маскированный номер карты
    """
    card_str = str(card_number)
    if len(card_str) != 16 or not card_str.isdigit():
        logger.error(f"Неверный номер карты: {card_number}. Должен содержать 16 цифр.")
        raise ValueError("Номер карты должен содержать 16 цифр")

    logger.info(f"Маскировка номера карты: {card_str[:6]}... успешно выполнена.")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счёта по формату **XXXX.

    :param account_number: Номер счёта (целое число)
    :return: Маскированный номер счёта
    """
    acc_str = str(account_number)
    if len(acc_str) < 4:
        logger.error(f"Неверный номер счёта: {account_number}. Должен содержать хотя бы 4 цифры.")
        raise ValueError("Номер счёта должен содержать хотя бы 4 цифры")

    logger.info(f"Маскировка номера счёта: ...{acc_str[-4:]} успешно выполнена.")
    return f"**{acc_str[-4:]}"
