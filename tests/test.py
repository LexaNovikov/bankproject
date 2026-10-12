from src.widget import get_date, mask_account_card

print("==========MASK_ACCOUNT_CARD==========")
with open("./mask_account_card.txt", "r") as file:
    data = file.readlines()
    for i in data:
        print(i, mask_account_card(i), sep="", end="\n=====================================\n")
print("\n=============GET_DATE=============")
with open("./get_date_tests.txt", "r") as file:
    data = file.readlines()
    for i in data:
        print(i, get_date(i), sep="", end="\n=====================================\n")
