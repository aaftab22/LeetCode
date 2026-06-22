# Write a program to create a byte type array, read, modify, and display the elements of the array
arr = bytearray([1,255,23,45])

# read
print(list(arr))

#modify
arr[1] = 1

#read
print(list(arr))

#display
for i in range(len(arr)):
    print(arr[i], end=" ")