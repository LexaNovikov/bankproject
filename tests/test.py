from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

filters_tests = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 3, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 4, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
    {"id": 5, "state": "EXECUTED", "date": "2020-02-01T12:00:00"},
    {"id": 6, "state": "EXECUTED", "date": "2020-03-01T12:00:00"},
    {"id": 7, "state": "CANCELED", "date": "2020-01-01T12:00:00"},
    {"id": 8, "state": "CANCELED", "date": "2020-02-01T12:00:00"},
    {"id": 9, "state": "EXECUTED", "date": "2020-05-15T15:30:00"},
    {"id": 10, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
    {"id": 11, "state": "CANCELED", "date": "2020-01-02T12:00:00"},
    {"id": 12, "state": "CANCELED", "date": "2020-01-03T12:00:00"},
]
print("==========MASK_ACCOUNT_CARD==========")
with open("tests/mask_account_card.txt", "r") as file:
    data = file.readlines()
    for i in data:
        print(i, mask_account_card(i), sep="", end="\n=====================================\n")
print("\n=============GET_DATE=============")
with open("tests/get_date_tests.txt", "r") as file:
    data = file.readlines()
    for i in data:
        print(i, get_date(i), sep="", end="\n=====================================\n")
print("\n============FILTERS_DOWN============")
print(*sort_by_date(filters_tests), sep="\n")
print("\n=============FILTERS_UP=============")
print(*sort_by_date(filters_tests, False), sep="\n")

print("\n============FILTERS_BY_STATE_EXECUTED============")
print(*filter_by_state(filters_tests, "EXECUTED"), sep="\n")
print("\n============FILTERS_BY_STATE_CANCELED============")
print(*filter_by_state(filters_tests, "CANCELED"), sep="\n")
