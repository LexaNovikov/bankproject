def filter_by_state(dictionaries_list: list[dict], key: str = "EXECUTED") -> list[dict]:
    result = []
    for i in dictionaries_list:
        if i["state"] == key:
            result.append(i)
    return result


def sort_by_date(dictionaries_list: list[dict], key: bool = True) -> list[dict]:
    len_of_result = 0
    result = []
    for i in dictionaries_list:
        result.append(i)
        len_of_result += 1
        idx = len_of_result - 1
        while idx > 0 and result[idx - 1]["date"] < result[idx]["date"]:
            result[idx - 1], result[idx] = result[idx], result[idx - 1]
            idx -= 1
    if key == False:
        result.reverse()
    return result
