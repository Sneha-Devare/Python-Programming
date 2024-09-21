#  if-elif-else(SYNTAX)
'''
   if(condition):
     statement1
   elif(condition):
     statement2
   else:
    statementN
'''

age=int(input("Enter your age :"))
if(age>= 18):
  print("You can vote") 
elif(0<age<18):
  print("You cannot vote")
else:
  print("You are not born yet")
  
