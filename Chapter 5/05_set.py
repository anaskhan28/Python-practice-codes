b =  set()
print(type(b))
# Accessing Elements 
b.add(4)
b.add(2)
b.add(2) # adding a value reapetedly doesnot change
b.add((4,5,7))
# b.add({4:5}) cannot add list or dictionary to sets
print(b)
# Length of the set
print(len(b)) # print the length of the set

# Removal of the set
b.remove(2) # remove 2 from set b
# b.remove(15) throws an error because the number is not present 
print(b)

print(b.pop())