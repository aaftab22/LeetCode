# Create a program to retrieve, display and update only a range of elements from an array using indexing and
# slicing in arrays
arr1 = [1,2,4,5,7,3,8,9]

# retrieve and display
arr2 = arr1[2:5]

# updating only the range
for i in range(2,5):
    arr1[i] += 2

print(arr1)
print(arr2)
