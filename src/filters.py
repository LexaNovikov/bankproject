import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция фильтрации операций по описанию"""
    return [operation for operation in data if re.search(search, operation.get("description", "")) is not None]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция подсчета количества операций по описанию"""
    operations = [operation.get("description") for operation in data if operation.get("description") in categories]
    counter = Counter(operations)
    return dict(counter)
