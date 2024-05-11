import json
from datetime import datetime


def get_data():
    """считывает данные"""
    with open("data/operation.json") as file:
        return json.load(file)


def filter_data(data):
    """фильтр по операциям Executed"""
    filter_operations = [operation for operation in data if "state" in operation and operation["state"] == 'EXECUTED']
    return filter_operations


def sort_operations(data):
    """Сортировка последних пяти операций и их вывод"""
    sorted_operation = sorted(data, key=lambda x: x["date"], reverse=True)
    return sorted_operation[:5]


def format_date(data):
    '''форматирует дату'''
    for el in data:
        date_str = el["date"].split('T')
        numbers = date_str[0].split('-')
        y_, m_, d_ = numbers
        el["date"] = '.'.join([d_, m_, y_])

    return data


def mask_transactions(data):
    '''маскриует счет и карту'''
    for transaction in data:
        if 'from' in transaction:
            from_parts = transaction['from'].split()
            if from_parts[0] == 'Счет':
                transaction['from'] = 'Счет **' + from_parts[-1][-4:]
            else:
                card_number = from_parts[-1]
                transaction['from'] = ' '.join(from_parts[:-1]) + ' ' + card_number[:4] + ' ' + card_number[4][:6] + '** ****' + ' ' + card_number[-4:]

        if transaction['to'].startswith('Счет'):
            transaction['to'] = 'Счет **' + transaction['to'].split()[-1][-4:]
        else:
            to_parts = transaction['to'].split()
            card_number = to_parts[-1]
            transaction['to'] = ' '.join(to_parts[:-1]) + ' ' + card_number[:4] + ' ' + card_number[4][:6] + '** ****' + ' ' + card_number[-4:]
    return data



#def format_amount(amount):
    #return amount['amount']


def format_transaction(data):
    """вывродит опреации в определенном формате"""
    #{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
    # 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
    # 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}

    #14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
    # 82771.72 руб.
    for transaction in data:
        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['name']
        if 'from' in transaction:
            print(f''''
            {transaction['date']} {transaction['description']}
            {transaction['from']} -> {transaction['to']}
              {amount} {currency}''')
        else:
            print(f''''
            {transaction['date']} {transaction['description']}
            {transaction['to']}
             {amount} {currency}''')


#def print_transactions(data):
    #for transaction in data:
        #print(format_transaction(transaction))







