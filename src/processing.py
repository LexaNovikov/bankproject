def filter_by_state(dictionaries_list: list[dict], key: str = "EXECUTED") -> list[dict]:
    """Функция для фильтрации логов по state"""
    result = []
    for data_dict in dictionaries_list:
        if data_dict["state"] == key:
            result.append(data_dict)
    return result


def sort_by_date(dictionaries_list: list[dict], key: bool = True) -> list[dict]:
    """Функция для сортировки логов по дате"""
    len_of_result = 0
    result = []
    for data_dict in dictionaries_list:
        result.append(data_dict)
        len_of_result += 1
        idx = len_of_result - 1
        while idx > 0 and result[idx - 1]["date"] < result[idx]["date"]:
            result[idx - 1], result[idx] = result[idx], result[idx - 1]
            idx -= 1
    if not (key):
        result.reverse()
    return result
