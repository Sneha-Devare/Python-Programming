#set is a collection of unordered items 
#each element in the set must be unique and immutable
#sets are mutable but its elements are immutable

nums={1,2,3,4}
set2={1,2,2,4}  #duplicate elements not allow so it will give only 1,2and 4 in output
print(set2)

null_set=set()        #empty set syntax


collection={1,2,3,4,"sneha","shubham"}
print(collection)
print(type(collection))
col2={1,1,1}       #we cannot store duplicate values   #set ignores duplicate values means it does not print it
print(col2)

#to print length of set
print(len(collection))

#add values to the set
collection.add(9)
collection.add("rohini")
print(collection)
 
#remove values from the set
collection.remove("rohini")
print(collection)

#removes a random value
collection.pop()
print(collection)

#empty the set
collection.clear()
print(collection)

#union
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))



