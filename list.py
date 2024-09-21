#list in python
#abuilt in datatype that stores list of values
#it can store elements of different types like int,float,string
#it is same like arrays of another languages
#we use square brackets for making any type of list
#strings are immutable where lists are mutable in python
#slicing is possible in lists


marks=[12.8,58.9,25.6,89.2,85.2,56.5]
print(marks)
print(type(marks))

students=["sneha",20,"belapur","shrirampur","ahmednagar","maharashtra","india"]
print(type(students[2]))  #type of belapur which is str
print(type(students[1]))  #type of 20 which is int

#accessing list
print(marks[0])
print(marks[0:5])

#to find length of string
print("length of string is :",len(marks))

#change values using indexing
students[1]=21
print(students)

#ERROR
# print(students[10])    #list index is out of range

#list functions/methods
list=[2,1,3]

list.append(4)  #adds one element at the end 
print(list)

list.sort()   #sort list in ascending order
print(list)
list.sort(reverse=True)    #sort list in descending order
print(list)

list.reverse()    #it reverses the list
print(list)

list.insert(5,"sneha")    #insert element at specific index
print(list)

list.remove(1)     #remove first occurence of the element
print(list)   

list.pop(2)    #removes element at index
print(list)
