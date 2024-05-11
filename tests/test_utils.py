from src.utils import format_date, mask_transactions


def test_format_date():
    assert format_date("2019-04-04T23:20:05.206878") == "04.04.2019"

def test_mask_transactions():
    assert mask_transactions("from": "Visa Gold 3654412434951162") == "Visa Gold 3654 41** **** 1162"

#def test_get_transactions():
    #assert get_transactions({"from": "Maestro 1308795367077170", "to": "Счет 96527012349577388612"}) ==
