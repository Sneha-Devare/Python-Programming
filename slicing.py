#Accessing parts of a string
#in slicing ending index is not included

# str="sneha devare"
# print(str[0:5])      #print char that are on index 0-5
# print(str[0:len(str)])    #print all string
# print(str[:3])     #print string from start till len(3)
# print(str[2:])    #print string from 2 till end of the string

#negative index in slicing
# print(str[-1])
# print(str[-2])
# print(str[-5:-1])
# print(str[-12:-1])  

#strinf functions
str="i am a coder."
print(str.endswith("er.") ) #returns true if string end with substr
print(str.capitalize())    #capitalize first character of string
print(str.replace("a",""))  #replaces all occurences of old with new
print(str.find("am"))    #returns first index of first occurence
#and if we enter character which is not in string will give output -1 which means not found or something

print(str.count("am"))   #count the occurences of substr in the given string