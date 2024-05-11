from src.utils import get_data, filter_data, sort_operations, format_date, mask_transactions, format_transaction

load_data = get_data()
filtered_data = filter_data(load_data)
sorted_operations = sort_operations(filtered_data)
formatted_data = format_date(sorted_operations)
masked_tr = mask_transactions(formatted_data)
result_transaction = format_transaction(masked_tr)


print(result_transaction)