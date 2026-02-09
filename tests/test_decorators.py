"""
Тесты для декоратора log.
"""

import os

import pytest

from src.decorators import log


@pytest.fixture
def log_file():
    """Фикстура: временный файл лога."""
    filename = "test_log.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


def test_log_to_file_success(log_file):
    """Тест: успешный вызов записывается в файл."""

    @log(filename=log_file)
    def add(a, b):
        return a + b

    add(3, 4)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "add ok" in content


def test_log_to_file_error(log_file):
    """Тест: ошибка записывается в файл с параметрами."""

    @log(filename=log_file)
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "divide error: ZeroDivisionError" in content
    assert "Inputs: (1, 0), {}" in content


def test_log_to_console_success(capsys):
    """Тест: успех выводится в консоль."""

    @log()
    def multiply(a, b):
        return a * b

    multiply(2, 3)

    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_to_console_error(capsys):
    """Тест: ошибка выводится в консоль с параметрами."""

    @log()
    def broken():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        broken()

    captured = capsys.readouterr()
    assert "broken error: ValueError. Inputs: (), {}" in captured.out
