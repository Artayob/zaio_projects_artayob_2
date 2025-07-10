def testfunc(x, y):
    print(f"First Arguement is {x}")
    print(f"Second Arguement is {y}")
    return x*y
print(testfunc(3, 5))
ret = testfunc(6, 7)
print(ret)
print(testfunc.__doc__)

print("-----------------------------------------------------------------")

def testfunc(x, y):
    print(f"First Arguement is {x}")
    print(f"Second Arguement is {y}")
    return x*y, x+y, x/y
print(testfunc(4, 8))

print("-----------------------------------------------------------------")

ret1, ret2, ret3 = testfunc(8, 9)
print(ret1)
print(ret2)
print(round(ret3, 2))

print("-----------------------------------------------------------------")

def testfunc(x, y):
    testvar_l = 7  # Available only within the function 
    print("testvar_g:", testvar_g)
    print(f"First Arguement is {x}")
    print(f"Second Arguement {y}")
    return x*y+testvar_g
testvar_g = 5
print(testfunc(4,5))

print("-----------------------------------------------------------------")