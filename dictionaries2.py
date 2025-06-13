# items return all the key value pairs in the forms of tuples

dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
dict_items = dict_tran.items()
print(dict_items)

print("---------------------------------------------------------------------------------------------------------------------------")

# Keys returns all the keys of the dictionary
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
dict_keys = dict_tran.keys()
print(dict_keys)

print("---------------------------------------------------------------------------------------------------------------------------")

# Keys returns all the keys of the dictionary
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
dict_values = dict_tran.values()
print(dict_values)

print("---------------------------------------------------------------------------------------------------------------------------")

# Setdefault insert a specific key value pair if the key exists returns value
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings', 'Amount_Drawn': 8000}
dict_tran.setdefault('New_field', 6766)
print("Printing the updated dictionary - pass 1: ", dict_tran)
ret = dict_tran.setdefault('Amount_Drawn', 6766)
print("Printing the updated dictionary - pass 2:", dict_tran)
print("Checking the retuened value:", ret)

print("---------------------------------------------------------------------------------------------------------------------------")

# Iterating through a ditionary
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings', 'Amount_Drawn': 8000}
for x in dict_tran:
    print("Key: ", x, " -- Value: ", dict_tran[x])