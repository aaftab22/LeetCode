# Write a program to understand various methods of array
# class mentioned: append, insert, remove, pop, index, tolist and count.
from array import *

lst1 = array('i',[1,2,3,4,5,6,7,8,9])

print(lst1)

lst1.remove(3)
print(lst1)

lst1.insert(2,3)
print(lst1)

lst1.append(10)
print(lst1)

lst1.pop()
print(lst1)

print(lst1.index(4))

lst1.reverse()
print(lst1)

lst1.sort()
print(lst1)

lst1.sort(reverse=True)
print(lst1)

lst1.extend(lst1)
print(lst1)

lst1.tolist()