#dictionary in python
#dictionaries are used to store data values in Key:value pairs
#they are unordered, mutable(changable) and don't allow duplicate keys
#keys are always unique

dict = {
    "name":"sneha",
    "cgpa":9.6,
    "marks":[98, 97, 95],
    "age":20,
    "is_adult":True,
    "subjects":("maths","english","bio")
}
print(dict)

#key can be string value, integer value or can also be float value
family = {
    1:"sneha",
    2:"shubham",
    3:"varsha",
    4:"mumma",
    5:"pappa"
}
print(family)
print(type(family))

#accessing elements using keys
print(family[2])
print(family[1])
print(family[3])
print(family[2])

print(type(family))

#adding new value to key
family[1]="didi"
print(family)

null_dict = {}     #to create null dictionary
print(null_dict)

#nested dictionaries

student={
    "name":"sneha",
    "score":
      {
          "chem":98,
          "phy":95,
          "maths":91
      }
}
print(student)
print(student["score"]["chem"])   #we can add more keys to get presize output

#dictionary methods

print(family.keys())    #return all keys
print(family.values())    #return all values
print(family.items())    #returns all keys,val pairs as tuples

#to find length of dictionary
print(len(family))

#to create list of dictionary
print(list(family.items()))

#to acccess it indidvidually
pairs=list(family.items())
print(pairs[2])

#to return values of key
print(family[2])    #without function    
print(family.get(2))   #with function 

#why here these two methods bcoz if we use function for it...we will not get any error it shows only "none" value while otherone will give error

#insert the specified items to the dictionary
family.update({3:"vahini"})
print(family)
