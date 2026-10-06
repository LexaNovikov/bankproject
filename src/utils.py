import json


def get_operations_data(path: str = "../data/operations.json") -> list[str]:
    """Функция для получения списка операций"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception:
        return []
