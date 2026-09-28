from functools import wraps

from mypy.nodes import Callable


def log(filename: str = "console") -> Callable:
    """Декоратор для логирования работы функции"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
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


@log()
def solve(x, b):
    return x + b


print(solve(1, 2))
