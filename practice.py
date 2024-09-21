# write a program to input 2 numbers and print their sum
# num1=int(input("Enter number1:"))
# num2=int(input("Enter number2:"))
# print("sum of num1 and num2 is :",num1+num2)



# write a program to input side of a square and print its area
# side=float(input("Enter side of Square:"))
# print("Area of Square is:",side*side)  #side**2



#write program to input 2 float numbers and print their average
# number1=float(input("enter number 1:"))
# number2=float(input("enter number 2:"))
# average=(number1+number2)/2
# print("Average is :",average)



#write a program to input 2 numbers a and b . Print true if a is greater than or equal to b and if not print false
# a=int(input("enter number 1:"))
# b=int(input("enter number 2:"))
# if(a>=b):
#     print(a>=b)
# else:
#     print(a>=b)



# #write a program to input user's first name and print its length
# First_name=input("enter your first name: ")
# print(len(First_name))



#write a program to find the occurence of "$" in a string
# str="Hi, $I am the $ symbol $99.99"
# print("times of",str.count("$"),"$ in it")




#write a program to check if a number entered by a user is odd or even
# number=int(input("enter any number: "))
# if(number%2==0):
#     print("number is even.")
# else:
#     print("number is odd.")




#write to find the greatest of three numbers entered by the user
# num1=int(input("enter no 1: "))
# num2=int(input("enter no 2: "))
# num3=int(input("enter no 3: "))
# if(num1==num2==num3):
#     print("these three numbers are equal.")
# elif(num1>=num2 and num1>=num3):
#     print("number 1 is greatest among them.")
# elif(num2>=num1 and num2>=num3):
#     print("number 2 is greatest among them.")
# elif(num3>=num2 and num3>=num1):
#     print("number 3 is greatest among them.")



#write a program if a number is multiple of 7 or not
# num=int(input("enter any number: "))
# if(num%7==0):
#     print("Given num is multiple of 7.")
# else:
#     print("Given num is not multiple of 7.")




#write a program to ask the user to enter names of their three favorite movies and store them in a list
# movies=[]
# movie1=input("Enter your First Favorite movie : ")
# movie2=input("Enter your Second Favorite movie : ")
# movie3=input("Enter your Third Favorite movie : ")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)
#OR
# movie=[]
# movie.append(input("Enter your First Favorite movie : "))
# movie.append(input("Enter your Second Favorite movie : "))
# movie.append(input("Enter your Third Favorite movie : "))
# print(movie)




#write a program to check if a list contains palindrome of elements
# user_input_list=input("enter items separated by spaces: ")
# lists=user_input_list.split()     #This function converts input into the list
# list_copy=lists.copy()
# print(lists)
# print(list_copy)
# list_copy.reverse()

# if(lists==list_copy):
#     print("list is a palindrome")
# else:
#     print("list is not a palindrome")



#write a program to count the number of students with the "A" grade in the following tuple.
grade=("C","D","A","A","B","B","A")
# students_count=grade.count("A")
# print(students_count)


#store the above values in a list and sort them from "A" to "Z"
grades=list(grade)
print(grades)
grades.sort()
print(grades)
