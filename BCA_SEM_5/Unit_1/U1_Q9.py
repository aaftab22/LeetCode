# Write a Menu driven Python program which perform the following:
# Find area of circle
# Find area of triangle
# Find area of square and rectangle
# Find Simple Interest
# Exit.( Hint: Use infinite while loop for Menu)

print("\n****************************************")
print("Welcome to the Python Menu program:\nThese are your options choose what you want to do.")
print("1. Find area of circle")
print("2. Find area of triangle")
print("3. Find area of square and rectangle")
print("4. Find Simple Interest")
print("5. Exit")
print("****************************************")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        radius = float(input("Please enter the radius of the circle = "))
        print("The area of the circle is", 3.14 * radius * radius)

    elif choice == 2:
        height = int(input("Please enter the height of the triangle = "))
        base = int(input("Please enter the base of the triangle = "))
        print("The area of the triangle is", 0.5 * height * base)

    elif choice == 3:
        length = int(input("Please enter the length of the rectangle/squre = "))
        width = int(input("Please enter the width of the rectangle/square = "))
        print("The area of the rectangle is", length * width)

    elif choice == 4:
        principal = int(input("Please enter the principal amount = "))
        interest = float(input("Please enter the interest rate = "))
        year = int(input("Please enter how many years = "))
        print("The total interest is ", principal * interest * year / 100 )

    elif choice == 5:
        print("Thank you for using this program")
        break
    else:
        print("Please choose from option 1 to 5 :) ")