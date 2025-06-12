# creating variables 
i = 5
print(i)
str = "Mya name is John Does"
print(str)
flt = 12.678
print(flt)
bln = True
print(bln)

#  Print the Type of each of the variables

print(type(i))
print(type(str))
print(type(flt))
print(type(bln))

# modulus 
i = 30
j = 7
print(i%j)

# Checking Conditions (Multiple Simultaneous Conditions)
x = 7 
y = 9
if x == 7 and y < 10:
    print("Condition not Met - Multiline Block")
    print("Conditon met")

else: 
    print("Condition not met - multiline Block")
    print("Condition not Met")    

# Multiple conditions
if x == y:
    print("equal")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")            

# Nested 'if'
x = 7 
y = 9 
if x < y:
    if x > 5:
        print("nested condition met")
    else:
        print("Inner nested False Block")
else:
    print("outer nested False Block")            