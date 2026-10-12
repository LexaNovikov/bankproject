from functools import wraps
from typing import Any

from mypy.nodes import Callable


def log(filename: str = "console") -> Callable:
    """Декоратор для логирования работы функции"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            try:
                res = func(*args, **kwargs)
                if filename == "console":
                    print(f"{func.__name__}, ok")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__}, ok\n\n")
                return res
            except Exception as e:
                if filename == "console":
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n\n")

        return wrapper

    return decorator
