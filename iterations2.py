# Example of a 'for' loop for a numeric range 

for x in range(5):
    print(x, "is being processed")    

# Example of a 'for' loop for a numeric range with custom start and end values 
for x in range(3, 8):
    print(x, "is being processed")       
# Example of a 'for' loop wiht a custom step
for x in range(2, 14, 2):
    print(x, "is being processed")

# Creating a custom range

def cust_range(start_val, end_val, step_val):
    while start_val <= end_val:
        yield start_val
        start_val += step_val

for x in cust_range(5, 25, 5):
    print(x)

# Example of 'break'ing away from a loop
for x in range(5, 31, 5):
    print(x, "is being processed")
    if x == 20:
        print("Breading away..")
        break

# Example of 'continuing' into a loop 
for x in range(5, 31, 5):
    if x == 20:
        print("Continue to the top of the loop")
        continue
    print(x, "is being processed")

# Example of 'pass' in a loop
for x in range(5, 31, 5):
    if x == 20:
        print("Continue to the top of the loop")
        pass
    print(x, "is being processed")