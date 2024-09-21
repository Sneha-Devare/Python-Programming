# This is recursive function example which means function call function itself
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
result=factorial(10)
print(result)
