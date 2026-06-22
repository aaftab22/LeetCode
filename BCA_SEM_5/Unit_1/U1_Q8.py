# Write a python program to find the sum of even numbers using command line arguments.
import sys

args = sys.argv[1:]
total = 0

for arg in args:
    num = int(arg)
    if num % 2 == 0:
        total += num

print("Total of all even number is = ", total)