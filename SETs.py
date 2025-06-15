# Creating a set 
set1 = set(['Gayle', 'Gilchrist', 'Waugh', 'Dravid', 'Pollock', 'Tendulkar', 'Ghavaskar', 'Dhoni'])
print(set1)
# Sets cannot have duplictaed values 

print("---------------------------------------------------------------------------------------------")

# Finding an intersection 

set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set(['a', 'b', 'c', 'e', 'f', 'h', 'm', 't', 'q'])
print("Set 1:", set1)
print("Set 2:", set2)
int1 = set1 & set2   # the & is means intersection 
int2 = set1.intersection(set2)
print("Intersection using & operator: ", int1)
print("Intersection using the Intersection method: ", int2)
if int1 == int2:
    print("The intersections are the same")

print("---------------------------------------------------------------------------------------------")

# Finding the union

set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set(['a', 'b', 'c', 'e', 'f', 'h', 'm', 't', 'q'])
print("Set 1:", set1)
print("Set 2:", set2)
uni1 = set1 | set2   # Use the '|' - union operator
uni2 = set1.union(set2)
print("Union using | operator: ", uni1)
print("Union using the Union method: ", uni2)
if uni1 == uni2:
    print("The Unions are the same")

print("---------------------------------------------------------------------------------------------")

# Finding the difference
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set(['a', 'b', 'c', 'e', 'f', 'h', 'm', 't', 'q'])
print("Set 1:", set1)
print("Set 2:", set2)
dif1 = set1 - set2   # Use the '-' - difference operator
dif2 = set1.difference(set2)
print("Difference using - operator: ", dif1)
print("Difference using the difference method: ", dif2)
if uni1 == uni2:
    print("The difference are the same")

print("---------------------------------------------------------------------------------------------")

# Finding the Symmetric difference
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set(['a', 'b', 'c', 'e', 'f', 'h', 'm', 't', 'q'])
print("Set 1:", set1)
print("Set 2:", set2)
dif1 = set1 ^ set2   # Use the '^' - for symmetric difference operator
dif2 = set1.symmetric_difference(set2)
print("Symmetric Difference using ^ operator: ", dif1)
print("Symmetric Difference using the symmetric_difference method: ", dif2)
if dif1 == dif2:
    print("The symmetric difference are the same")

print("---------------------------------------------------------------------------------------------")

# Adding an element in a set 
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print("Set 1:", set1)
set1.add('i')
print("Updated Set1: ", set1)

print("---------------------------------------------------------------------------------------------")

# Check if element c is a part of the set
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print("Whether c is pressent in Set1: ", 'c' in set1)
print("Whether c is pressent in Set1...negative way: ", 'c' not in set1)

print("---------------------------------------------------------------------------------------------")

# Check for subset or superset
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set(['b','e', 'f', 'h'])
print("Set 1:", set1)
print("Set 2:", set2)
print("Whether Set2 is a subset of set1: ", set2.issubset(set1))
print("Whether Set1 is a superset of set2: ", set1.issuperset(set2))

print("---------------------------------------------------------------------------------------------")

# Len finds the the number of elements in a set
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(len(set1))

print("---------------------------------------------------------------------------------------------")

# Copy the set 
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set1.copy()
print("Printing original set: ", set1)
print("Printing the copied set: ", set2)
print("Memory Address of Set1: ", id(set1))
print("Memory Address of Set2: ", id(set2))
if id(set1) != id(set2):
    print("Shallow Copy")

print("---------------------------------------------------------------------------------------------")

# Remove an element from the set
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set1.remove('d')
print(set1)

print("---------------------------------------------------------------------------------------------")

# Pop removes an element from the set
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
x = set1.pop()
print("Popped Item: ", x)
print("New Set: ", set1)

print("---------------------------------------------------------------------------------------------")

# Difference update 
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set(['b', 'e', 'f', 'h', 'u', 'j'])
set1.difference_update(set2)
print("Difference update: ", set1)

print("---------------------------------------------------------------------------------------------")

#Symmetric Difference update 
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
set2 = set(['b', 'e', 'f', 'h', 'u', 'j'])
set1.symmetric_difference_update(set2)
print("Symmetric Difference update: ", set1)

print("---------------------------------------------------------------------------------------------")

# Itterating through a set
# Traversing through a set
set1 = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
for x in set1:
    print(x)