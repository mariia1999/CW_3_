from src.utils import format_date, mask_transactions


def test_format_date():
    test_date = [
        {"date": "2019-04-04T23:20:05.206878"}
    ]
    formatted_date = format_date(test_date)
    assert formatted_date[0]["date"] == "04.04.2019"


def test_mask_transactions():
    test_transactions = [
        {"from": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472"}
    ]
    masked_transaction = mask_transactions(test_transactions)
    assert masked_transaction[0]["from"] == "Visa Gold 5999 41** **** 6353"
    assert masked_transaction[0]["to"] == "Счет **4472"





