import json


def get_operations_data() -> list[str]:
    """Функция для получения списка операций"""
    try:
        with open("../data/operations.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        return []
