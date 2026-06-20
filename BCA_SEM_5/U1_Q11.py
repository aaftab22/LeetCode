#Program to search an element in the list using for loop and also demonstrate the use of “else” with for loop.
lst = [1,2,3,4,5,6,7,8,9,0]
search = int(input("Please enter a number to search for: "))
for i in lst:
    if search == i:
        print("Element in the list")
        break
else:
    print("Element is not in the list")
