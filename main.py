from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions_from_json
from src.widget import get_date, mask_account_card

# Тестирование mask_account_card
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))

# Тестирование get_date
print(get_date("2024-03-11T02:26:18.671407"))

# Тестирование sort_by_date
operations_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Сортировка по убыванию (по умолчанию)/возрастанию
sorted_descending = sort_by_date(operations_data)
print(sorted_descending)

sorted_ascending = sort_by_date(operations_data, reverse=False)
print(sorted_ascending)

# Сортировка по статусу
sorted_executed = filter_by_state(operations_data)  # EXECUTED
print(sorted_executed)

sorted_canceled = filter_by_state(operations_data, "CANCELED")  # CANCELED
print(sorted_executed)

# Тест маскировки
try:
    print(get_mask_card_number(7000792289606361))  # 7000 79** **** 6361
    print(get_mask_account(73654108430135874305))  # **4305
except ValueError as e:
    print(f"Ошибка: {e}")

# Тест загрузки
transactions = load_transactions_from_json("data/operations.json")
print(f"Загружено транзакций: {len(transactions)}")
