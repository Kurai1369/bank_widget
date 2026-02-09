"""
Модуль для взаимодействия с внешним API.
"""

import os

import requests


def convert_currency(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта USD или EUR.

    :param transaction: Словарь с данными о транзакции
    :return: Сумма в рублях
    """
    operation_amount = transaction.get("operationAmount", {})
    currency = operation_amount.get("currency", {}).get("code")

    if currency == "RUB":
        return float(operation_amount["amount"])

    amount = float(operation_amount["amount"])
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/latest"

    headers = {"apikey": api_key}
    params = {"base": currency, "symbols": "RUB"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"]["RUB"]
        return float(amount * rate)

    except (requests.RequestException, KeyError, ValueError, TypeError):
        return 0.0

    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")
        return 0.0

    except (KeyError, IndexError) as e:
        print(f"Ошибка структуры ответа: {e}")
        return 0.0

    except (ValueError, TypeError) as e:
        print(f"Ошибка преобразования данных: {e}")
        return 0.0
