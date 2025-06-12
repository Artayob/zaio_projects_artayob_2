# Example of definite iteration
l = 5
m =0
i = 0
while l > 0:
    m += l
    l -= 1
    i += 1
    print("Iteration", i)
print("Final value of m =", m)

# Example of a 'for' loop for a list
Weekdayslist = ["Sunday", "Monday", "Tuesday"] 
for x in Weekdayslist:
    print(x)

# Example of a 'for' loop for a tuple

CountryTuple = ("India", "US", "UK", "Germany")
for x in CountryTuple:
    print(x)

# Example of a 'for ' loop for a set
PlayerSet = {"Ronaldo", "Messi", "Neymar"}   
for x in PlayerSet:
    print(x) 

# Example of a 'for' loop for a dictionary
PersonDict = {"Name": "Abdurrahmaan Tayob", "Age": 18, "Salary": 20000}
for x in PersonDict:
    print(x, PersonDict[x])    

# Example of a 'for' loop of a string 
strx = "John Doe"
for x in strx:
    print(x)    

# Example of a 'for' loop for a numeric range 
for x in range(5):
    print(x, "is being processed")    