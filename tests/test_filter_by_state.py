from src.processing import filter_by_state


def test_filter_by_state(data_filter_list: list[dict]) -> None:
    assert filter_by_state(data_filter_list) == [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2020-02-01T12:00:00"},
        {"id": 6, "state": "EXECUTED", "date": "2020-03-01T12:00:00"},
        {"id": 9, "state": "EXECUTED", "date": "2020-05-15T15:30:00"},
        {"id": 10, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
    ]
    assert filter_by_state([]) == []
    assert filter_by_state(data_filter_list, "CANCELED") == [
        {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 7, "state": "CANCELED", "date": "2020-01-01T12:00:00"},
        {"id": 8, "state": "CANCELED", "date": "2020-02-01T12:00:00"},
        {"id": 11, "state": "CANCELED", "date": "2020-01-02T12:00:00"},
        {"id": 12, "state": "CANCELED", "date": "2020-01-03T12:00:00"},
    ]
    assert filter_by_state([], "nice") == []
    assert filter_by_state(data_filter_list, "") == []
    return
