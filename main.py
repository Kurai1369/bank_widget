from src.widget import get_date, mask_account_card

# Тестирование mask_account_card
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))

# Тестирование get_date
print(get_date("2024-03-11T02:26:18.671407"))
