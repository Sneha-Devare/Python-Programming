#function in python 
#block of statement that perform a specific task

#def funct_name(parameter1,parameter2..)                 #function defination
#some work
#return val

#funct_name(arg1,arg2...)                                #function call


#sum function
# def sum(a,b):
#     sum=a+b
#     return sum
#     print(sum)
    
# print(sum(2,3) )                       #function call
        

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

output=print_hello()
print(output)          #none  #because it does not return any value


#default parameter
def product(a=1,b=1):      #default parameter   #if we pass nothing as a argument in function call then it will take that values that pass as a default
    product=a*b
    return product

print(product())          #1
print(product(56))
print(product(a=20))
print(product(20,10))