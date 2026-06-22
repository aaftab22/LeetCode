# Write a python program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the
# length to inches and print out the result. (2.54 = 1 inch).
cm = float(input("Enter in the length in CM: "))
if cm < 0:
    print("The length is invalid, please enter a positive number")
else:
    print("The length in inch = ", cm/2.54)

