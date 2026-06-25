 # Write a program to show variable length argument and its use.
def sum_all(*lst):
    result = 0
    for n in lst:
        result += n
    print(result)

def display_dictionary(**kwargs):
    for key, value in kwargs.items():
        print("key", key, " Value", value)

# variable length arguments
sum_all(1,2,3,4,5,6,7,8,9)

display_dictionary(name='Alice', age=30, city="New York")

