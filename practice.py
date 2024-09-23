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
# grade=("C","D","A","A","B","B","A")
# students_count=grade.count("A")
# print(students_count)


#store the above values in a list and sort them from "A" to "Z"
# grades=list(grade)
# print(grades)
# grades.sort()
# print(grades)


#store the following values in dictionary
# dictionary={"cat":"a small animal","table":["a piece of furniture" , "a list of facts"]}


#you are given a list of subjets for students. Assume one classroom is required for 1 subject .how many classrooms are required by all 
# students1={"python","java","c++","python","javascript"}
# students2={"java","python","java","c++","c"}
# Classroom=students1.union(students2)
# print(Classroom)
# print(len(Classroom)," classrooms are needed.")


#write a program to enter marks of 3 subjects from the user and store them into dictionary.start with an empty dictionary and add one by one.use subject name as key and marks as values.
# dict={}
# math=(int(input("enter marks of maths : ")))
# dict.update({"maths":math})
# phy=(int(input("enter marks of phy : ")))
# dict.update({"phy":phy})
# chem=(int(input("enter marks of chem : ")))
# dict.update({"chem":chem})
# print(dict)

#figure out a way to store 9 and 9.0 as separate values in a set(you can take help of built in data types)
# values={9,"9.0"}
# print(values)

# val={("float",9.0),
#      ("int",9)
#      }
# print(val)

# #print numbers from 1 to 100
# i=1
# while (i<=100):
#     print(i)
#     i=i+1


#print numbers from 100 to 1
# i=100
# while(i>=1):
#     print(i)
#     i=i-1
  

#print the multiplication table of a number n
# n=int(input("enter any no : "))
# i=1
# while(i<=10):
#     print(i*n)
#     i=i+1


#print rhe elements of the following list using a loop
#{1,4,9,16,25,36,49,64,81,100}

# i=1
# while(i<=10):
#     print(i*i)
#     i=i+1


#search for a number x in this tuple using loop:
#{1,4,9,16,25,36,49,64,81,100}

# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while(i<len(nums)):
#     if(nums[i]==x):
#         print("found",i)
#     i=i+1



#print the elements using for loop
#[1,4,9,16,25,36,49,64,81,100]

# tup=[1,4,9,16,25,36,49,64,81,100]
# for elements in tup:
#     print(elements)


#search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
# nums=[1,4,9,16,25,36,49,64,81,100,]
# x=49
# idx=0
# for elements in nums:
#     print("finding")
#     if(elements==x):
#         print("found",idx)
#     print("still searching")
#     idx=idx+1
# print("elements are ended")


#use range()

#print numbers from 1 to 100
# for nums in range (1,101):
#     print(nums)

#print numbers from 100 to 1
# for nums in range (100,0,-1):
#     print(nums)
          

#print the multiplication table of a number n
# x=int(input("enter any number: "))
# for nums in range(1,11):
#     print(nums*x)



#write a program to find the sum of first n natural numbers(using range)
# n=int(input("enter any number : "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("total sum : ",sum)

#using while above que
# n=int(input("enter any number : "))
# sum=0
# i=1
# while(i<=n):
#     sum+=i
#     i=i+1
# print("sum is : ",sum)



#write a program to find factorial of first n numbers(using for)
# n=int(input("enter any number : "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial is : ",fact)