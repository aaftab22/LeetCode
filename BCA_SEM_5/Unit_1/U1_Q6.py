# Create a program to display memory locations of two variables using id() function, and
# then use identity operators two compare whether two objects are same or not.

name = "Aaftab"
name2 = "Aaftab"

print(id(name))
print(id(name2))

print(name is name2)
