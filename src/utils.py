import json
import os

from mypy.types import Any

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_operations_data(path: str = os.path.join(base_dir, "data", "operations.json")) -> list[dict] | Any:
    """Функция для получения списка операций"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        return []
