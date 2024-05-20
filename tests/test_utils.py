from src.utils import format_date, mask_transactions, filter_data, sort_operations


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


def test_filter_data():
    test_data = [
        {
            "id": 147815167,
            "state": "EXECUTED"
        },

        {
            "id": 476991061,
            "state": "CANCELED"
        }
    ]
    filtered_data = filter_data(test_data)
    expected_result = [{
            "id": 147815167,
            "state": "EXECUTED"
        }]
    assert filtered_data == expected_result


def test_sort_operations():
    test_operations = [
        {"date": "2023-01-05", "state": "EXECUTED"},
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-03", "state": "EXECUTED"},
        {"date": "2023-01-04", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "EXECUTED"},
        {"date": "2023-01-06", "state": "EXECUTED"}
    ]
    expected_result = [
        {"date": "2023-01-06", "state": "EXECUTED"},
        {"date": "2023-01-05", "state": "EXECUTED"},
        {"date": "2023-01-04", "state": "EXECUTED"},
        {"date": "2023-01-03", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "EXECUTED"}
    ]
    assert sort_operations(test_operations) == expected_result






