#tuples are enclosed in()
#tuples are immutable

tup=(1,2,3,4,5)       #creating tuple with values
print(type(tup))
tuple=()              #empty tuple
print(type(tuple))
tup2=(1,)             #tuple with only one element
tup3=(1)              #if we write tuple with only one element like this that is without comma, then python is consider it as a integer or a string ...so always give comma at the end 
print(type(tup3))


#tuple methods
tup4=(2,1,3,1)

print(tup4.index(1))  #returns index of first occurence
print(tup4.count(1))  #count total occurences
