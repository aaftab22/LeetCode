# Write a program to generate prime numbers with the help of a function to test prime or not.
import math

def prime (rangeN):
    for i in range(2,rangeN):
        isPrime = True

        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            print(i)

n = int(input("In 0...N Enter the value of N:"))
prime(n)