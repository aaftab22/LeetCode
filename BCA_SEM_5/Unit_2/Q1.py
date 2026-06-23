# Write a program to create one array from another array.
arr1 = [3,4,5,3,21]

# arr2 = arr1.copy()

# list slicing
# arr2 = arr1[:]
arr2 = []
for i in arr1:
    arr2.append(i)

print("Array 1 = " , arr2)
print("Array 2 = " , arr2)