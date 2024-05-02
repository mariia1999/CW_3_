from src.utils import get_data, filter_data, sort_operations, format_date, format_transaction, print_transactions

load_data = get_data()
filter_ = filter_data(load_data)
sort_ = sort_operations(filter_)
#format_ = format_date(sort_)
format_tr = format_transaction(load_data)


#print_transactions(sort_)

#program = print_transactions(load_data)
print(format_tr)