# Write a program to demonstrate the use of Positional
# argument, keyword argument and default arguments.
def substraction (a, b=10):
    return a-b

x = int(input("Add value of X = "))
y = int(input("Add value of Y = "))

# default arguments
result = substraction(x)
print(result)

#positional argument
result = substraction(10, 20)
print(result)

# keyword argument
result = substraction(b=x, a=y)
print(result)