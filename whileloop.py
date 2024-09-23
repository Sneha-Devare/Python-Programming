#loops in python
#loops are used to repeat instructions

#while loop
# count=1           #iterators
# while (count<=10000):
#     print("hello,Sneha",count)
#     count=count+1

#print numbers from 1 to 10
# i=1
# while (i<=10):
#     print(i)
#     i=i+1

# #print numbers from 10 to 1
# i=10
# while (i>=1):
#     print(i)
#     i=i-1

#break and continue
#break:use to terminate loop when encountered
#continue:terminates execution in the current iteration and continues execution of the loop with the next iteration


#break
# i=1
# while(i<=10):
#     print(i)
#     if(i==8):
#         break
#     i=i+1


#continue
i=0
while i<=100:
    if(i%2==0):
        i=i+1
        continue
    print(i)
    i=i+1
    