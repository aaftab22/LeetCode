# Write a program to assert the user enters a number greater than zero.
num = int(input("Enter a number: "))

assert num > 0, "Number must be greater than zero"

print("You entered:", num)