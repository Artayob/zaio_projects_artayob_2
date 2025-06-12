tup1 = ()
print("Contents of an empty tuple: ", tup1)
tup1 = (1,2,3,4,5)
print("Contents of a simple Tuple: ", tup1)
tup1 = (1,2,(5,6,7), 4,5)
print("Conetents of a nested Tuple: ", tup1)
tup1 = (1,2,(5,6,7),4,[9,8,7])
print("Contents of a tuple having a nested list: ", tup1)
tup1  = ('Rohit', 'Karnataka', True, 2000)
print("Contents of a Tuple having mixed data types:", tup1)

print("-------------------------------------------------------")

# Creating tuple using tuple function 
lst1 = [1,2,3,4,5]
tup1 = tuple(lst1)
print("Print tuple created from list ", tup1)
dict1 = {'Name': "Robert", 'Salary': 2000}
tup2 = tuple(dict1)
print("Print tuple created fro dictionary", tup2)
str1 = "Christiano Ronaldo"
tup3 = tuple(str1)
print("Print uple created from string ", tup3)

print("----------------------------------------------------------------------")

# Accessing tuples with relative positioning 
tup1 = ('Jimi', 5000, True, 3.8, 2019, 300)
print("Print the 3rd Element of tup1:", tup1[2])
print("Print the 3rd Element of tup1:", tup1[-4])

print("--------------------------------------------------------------")

# you can use the same thing as a list to get chunks of the tuple eg print(tup1[1:5])
tup1 = ('Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock')
print(tup1[1:5])
print(tup1[:5])
print(tup1[1:])

print("--------------------------------------------------------------------------------")

# Access cross section of lists with stride 
tup1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(tup1[1:12:2])

print("--------------------------------------------------------------------------------")

# Index - Returns zero-based (positive) index of the first element matching the value 

tup1 = (1,3,7,8,7,5)
print(tup1.index(8))

print("--------------------------------------------------------------------------------")

# Count returns the number of time the number was passed 
tup1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(tup1.count(5))

print("--------------------------------------------------------------------------------")

# Any returns true if any of the elements are true 
tup1 = (1,2,3,4,5,6,7,8)
tup2 = (0,0)
print(any(tup1))
print(any(tup2))

print("--------------------------------------------------------------------------------")

# all returns true if all the elements in a tuple are true
tup1 = (1,2,3,4,0,6,7,8)
tup2 = (1,1,1,1)
print(all(tup1))
print(all(tup2))

print("--------------------------------------------------------------------------------")

# Enumerate adds a sequence number 
tup1 = ('Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock')
print(list(enumerate(tup1)))

print("--------------------------------------------------------------------------------")

# zip is a built in python function that takes in 2 sequences and returns a combined pair set
tup1 = (1,2,3,4,5)
tup2 = ('Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock')
print(list(zip(tup1,tup2)))

print("--------------------------------------------------------------------------------")

# Sorted - Returns a sorted lisr of the passed tuple 
res = sorted(('Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock'))
print("Sorted", res)
rev = sorted(('Gayle', 'Cilchrist', 'Waugh', 'Dravid', 'Pollock'), reverse = True)
print("Reverse Sorted", rev)

print("--------------------------------------------------------------------------------")

# Max returns the max value of a tuple 
tup1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(max(tup1))

print("--------------------------------------------------------------------------------")

# Min returns the min value of a tuple 
tup1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(min(tup1))

print("--------------------------------------------------------------------------------")

# Sum will return the sum of the tuple
tup1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
print(sum(tup1))

print("--------------------------------------------------------------------------------")

# Copying using deepcopy 
from copy import deepcopy 
tup1 = (1,2,3,4,5)
tup2 = deepcopy(tup1)
print("Copy: ", tup2)
print(id(tup1))
print(id(tup2))

print("--------------------------------------------------------------------------------")