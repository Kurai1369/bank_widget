"""
Основной модуль для взаимодействия с пользователем.
"""

from src.data_loaders import load_transactions_from_csv, load_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.search import search_transactions_by_description
from src.utils import load_transactions_from_json
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = load_transactions_from_json("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = load_transactions_from_csv("data/transactions.csv")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = load_transactions_from_excel("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор.")
        return

    available_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы:", ", ".join(available_states))
        state = input().upper().strip()
        if state in available_states:
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    filtered_transactions = filter_by_state(transactions, state)
    print(f'Операции отфильтрованы по статусу "{state}"')

    print("Отсортировать операции по дате? Да/Нет")
    sort_choice = input().lower().strip()
    if sort_choice == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        order = input().lower().strip()
        reverse = False if "возрастанию" in order else True
        filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse)

    print("Выводить только рублевые транзакции? Да/Нет")
    rub_only = input().lower().strip()
    if rub_only == "да":
        filtered_transactions = [
            t for t in filtered_transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    search_choice = input().lower().strip()
    if search_choice == "да":
        search_term = input("Введите слово для поиска: ").strip()
        filtered_transactions = search_transactions_by_description(filtered_transactions, search_term)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    for t in filtered_transactions:
        date_str = t.get("date", "")
        description = t.get("description", "")
        amount = t.get("operationAmount", {}).get("amount", "N/A")
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "N/A")
        account_from = t.get("from", "")
        account_to = t.get("to", "")

        print(f"\n{get_date(date_str)} {description}")
        if account_from:
            print(f"{mask_account_card(account_from)} -> ", end="")
        print(mask_account_card(account_to))
        print(f"Сумма: {amount} {currency}")


if __name__ == "__main__":
    main()
