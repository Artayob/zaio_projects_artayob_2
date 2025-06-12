# Create a list with multiple types of Data and Change them after creation
lst1 = ['Jimi', 5000, True, 3.8, 2019, 300]
print(lst1)
lst1[1] = 7000
print("Demonstarte Mutability :", lst1)

# Access lists with relative Positioning 
lst1 = ['Jimi', 5000, True, 3.8, 2019, 300]
print("Print the 3rd element of lst1: ", lst1[2])
print("Print the 3rd element of lst1: ", lst1[-4])

# Access cross section of Lists
lst1 = ['Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock']
print(lst1[1:5])
print(lst1[:5])
print(lst1[1:])

# Access cross section of lists with stride 
lst1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(lst1[1:12:2])

# Adding single elements in lists
lst1 = [1,2,3,4,5,6,7,8,9,10]
for x in range(5):
    lst1.append(x)
print(lst1)    

# Adding multiple elements to the list 
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst1.extend([11,12,13,14])
print(lst1)

# Removing an element using the pop method 
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst1.pop()
print("After pop: ", lst1)
lst1.pop(3)
print("After pop of the 4th element: ", lst1)

# Removing things from a list using remove method 
lst1 = ['Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock']
lst1.remove('Waugh')
print(lst1)

# Removing an element using the del keyword 
lst1 = ['Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock']
del lst1[2:4]
print(lst1)