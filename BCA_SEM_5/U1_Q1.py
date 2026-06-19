# Write a program to swap two numbers without taking a temporary variable.
num1 = int(input("Enter value for Num 1 = "))
num2 = int(input("Enter value for Num 2 = "))

print("Value before the swap: ")
print("Num 1 = " , num1 , "\nNum 2 = " , num2)

num1, num2 = num2, num1

print("Value after the swap: ")
print("Num 1 = " , num1 , "\nNum 2 = " , num2)