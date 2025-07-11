from time import time_ns

def cubed(x):
    return x**3

lambda_cubed = lambda x:x**3

start = time_ns()

print(f"Cube of 9 is {cubed(9)}")
print(f"Time taken by traditional method : {(time_ns()-start)//1000} ms\n")

start = time_ns()
print(f"Cube of 9 is {lambda_cubed(9)}")
print(f"Time taken by named Lambda method : {(time_ns()-start)//1000} ms\n")

start = time_ns()
print(f"Cube of 9 is {(lambda x:x**3)(9)}")
print(f"Time taken by inline Lambda function : {(time_ns()-start)//1000} ms\n")
print("--------------------------------------------------------------------------")

# Using map function 
numbers = [4, 5, 7, 7 , 9, 12, 23]
mapped_numbers = list(map(lambda x: x^3 + x^2 + 5*x -8, numbers)) # Leads to a list of values 
print(mapped_numbers)

print("--------------------------------------------------------------------------")
# Reduce function 
def cumul(a, b):
    result = a*b
    print(f'{a} * {b} = {result}')
    return result
print(cumul(4,5))

numbers = [4, 5, 6, 3, 8]
from functools import reduce  # reduce functio leads to only one value
out = reduce(cumul, numbers)
print(out)

print("-------------------------------------------------------------------------")

# Reduce now using the lambda function
cumul_l = lambda x,y: x*y
out1 = reduce(cumul_l, numbers)
print(out1)