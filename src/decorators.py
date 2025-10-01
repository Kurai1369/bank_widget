"""
Модуль для декораторов.
"""

import functools
import traceback
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который записывает в лог вызов функции и её результат.

    :param filename: Имя файла для записи лога. Если не указано — вывод в консоль.
    :return: Декорированная функция
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                message = f"{func_name} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message.strip())
                return result
            except Exception as e:
                error_type = type(e).__name__
                tb = traceback.format_exc()
                message = f"{func_name} error: {error_type}. Inputs: {args}, {kwargs}\n{tb}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message.strip())
                raise

        return wrapper

    return decorator
