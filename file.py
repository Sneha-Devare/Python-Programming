#file handling
#file input/output in python
#python can used to perform operation on files(read and write data)
  


#open ,read and close file
# f=open("C:\\Users\\sneha\\Desktop\\shubham.txt","r")
# data=f.read()      #returns the data in the form of streams
# data=f.read(2)      #it means it read only first 5 letters
# data=f.readline()    #it reads data line by line
# print(data)
# print(type(data))
# f.close()         #we should close the file


#write in file means overwrite....means it delete all the data of file....then write the new data
#if we perform a read function then it reads all from file and cursor is at the end of thst file....and after that we perform readline() then it will print only empty line because no data is their now....so if we want to perform that readline function we have to open file one more time....and execute that function.


# #writing a file  #overwrite mode
# f=open("C:\\Users\\sneha\\Desktop\\shubham.txt","w")
# f.write("this is new line")     #overwrites the entire file

# f=open("C:\\Users\\sneha\\Desktop\\shubham.txt","a")
# f.write("this is a new line")   #adds to the file   #add ata the end



#with syntax    #it will close file automatically
# with open ("C:\\Users\\sneha\\Desktop\\shubham.txt","r") as F:
#     data=F.read()
#     print(data)


#deleting a file
#using the os module
#module(like a code library) is a file written by the another programmer that generally has a function we ca use

import os
os.remove("C:\\Users\\sneha\\Desktop\\timepass.txt")



