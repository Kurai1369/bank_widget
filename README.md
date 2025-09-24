[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=BANK+WIDGET)](https://git.io/typing-svg)
![иконка_банка](https://img.icons8.com/nolan/96/bank-building.png)

---
### 📌 Описание
Проект для банковского виджета. Реализует маскировку данных, фильтрацию транзакций и генерацию номеров карт.

### 📁 Структура проекта
```
bank_widget/
├── src/
│ ├── __init__.py
│ ├── generators.py
│ ├── masks.py
│ ├── processint.py
│ └── widget.py
├── tests/
│ ├── __init__.py
│ ├── conftest.py
│ ├── test_generators.py
│ ├── test_masks.py
│ ├── test_processint.py
│ └── test_widget.py
├── .coverage
├── .flake8
├── README.md
├── main.py
└── pyproject.toml
```
### ⚙️ Установка и использование
```bash
git clone git@github.com:Kurai1369/bank_widget.git
cd bank_widget
poetry install
```
### ▶️ Запуск программы
```
python main.py
```
Активируйте окружение (если нужно):
```
poetry env activate | Invoke-Expression
```
### 📚 Документация
- [isort](https://pycqa.github.io/isort/) — сортировка импортов
- [Poetry](https://python-poetry.org/docs/) — управление зависимостями
#### 5️⃣ Лицензия.
Этот проект лицензирован по [MIT © Kurai](https://github.com/ryo-ma/github-profile-trophy/blob/master/LICENSE).

### 🧪 Тестирование
Проект протестирован с помощью `pytest`. Покрытие кода — более 80%.
```bash
poetry run pytest
poetry run pytest --cov=src --cov-report=html
start htmlcov/index.html
```

### 🚀 Примеры использования
#### Маскировка карты и счёта
```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
# → Visa Platinum 7000 79** **** 6361

print(mask_account_card("Счет 73654108430135874305"))
# → Счет **4305
```
#### Преобразование даты
```python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))
# → 11.03.2024
```
#### Фильтрация транзакций по валюте
```python
from src.generators import filter_by_currency

usd_transactions = list(filter_by_currency(transactions, "USD"))
# Вернёт список всех операций в долларах
```
#### Генерация номеров банковских карт
```python
from src.generators import card_number_generator

for number in card_number_generator(1, 4):
    print(number)
# → 0000 0000 0000 0001
# → 0000 0000 0000 0002
# → 0000 0000 0000 0003
```

### 🔗 Полезные ссылки

- [isort](https://pycqa.github.io/isort/) — сортировка импортов
- [Black](https://black.readthedocs.io/en/stable/) — форматирование кода
- [Pytest](https://docs.pytest.org/en/latest/) — тестирование
- [Poetry](https://python-poetry.org/docs/) — управление зависимостями
- [mypy](https://mypy.readthedocs.io/en/stable/) — статическая типизация
- [PEP 8](https://pep8.org/) — руководство по стилю кода