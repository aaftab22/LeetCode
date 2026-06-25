# Create a program to search the position of an element in
# an array using index() method of array class.
from array import *

arr = array('i',[11,2,6,4,3,5,8,1,9])

srch = int(input("Enter the element to find = "))

print(arr.index(srch))