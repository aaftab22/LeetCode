# Write a program to swap two numbers without taking a temporary variable.
num1 = 10
num2 = 20

print(num1)
print(num2)

num2 = num1 + num2
num1 = num2 - num1
num2 = num2 - num1

print("Num 1= " , num1 , "Num 2" , num2)