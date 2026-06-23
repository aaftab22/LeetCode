# Write a program to sort the array elements using bubble sort technique.
from array import *

arr = array('i',[11,2,6,4,3,5,8,1,9])

for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)