# Create our first dictionary 
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout'}
print(dict_tran)

#Create a dictinary with a list of the values 
dict_tran = {'Cust_id': 'C0876', 'Cust_trans': ['T001', 'T003', 'T006']}
print(dict_tran)

print("---------------------------------------------------------------------------------------")

# Populate from an empty dictionary 
dict_tran = {}
dict_tran['Cust_id'] = 'C0789'
dict_tran['Cust_trans'] = 'T001'
print(dict_tran)

print("---------------------------------------------------------------------------------------")

# Access dictionary elements by using keys to access 
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout'}
print("Printing value of Tran_id:", dict_tran['Tran_id'])
print("Printing value of Cust_id:", dict_tran['Cust_id'])

print("---------------------------------------------------------------------------------------")

# Deleting an element from a dictionary 
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout'}
del dict_tran['ATM_Location']
print("Printing the updated dictionary: ", dict_tran)

print("---------------------------------------------------------------------------------------")

# Deleting an element from a dict using pop and catching 'KeyError
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
try:
    popped = dict_tran.pop('Acc_Type')
    print("Printing the updated dictionary: ", dict_tran)
    print("What did i pop?", popped)
except KeyError:
    print("Key specified is not found in dict_tran")    

print("---------------------------------------------------------------------------------------")

# 'Clear' clears the entire dictionary
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
dict_tran.clear()
print(dict_tran)

print("---------------------------------------------------------------------------------------")

# Copy copies the dict
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
dict_copy = dict_tran.copy()
print(dict_copy)

print("---------------------------------------------------------------------------------------")

# Creates a new dict from specified keys 
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
keys = {'Cust_id', 'Acc_Type'}
dict_copy = dict_tran.fromkeys(keys)
print(dict_copy)

print("---------------------------------------------------------------------------------------")

# Geat gets the value
dict_tran = {'Tran_id': 'T0089', 'Cust_id': 'C000876', 'ATM_Location': 'HSR Layout', 'Acc_Type': 'Savings'}
dict_get = dict_tran.get('Cust_id')
print(dict_get)