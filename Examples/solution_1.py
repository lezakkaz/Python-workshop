# Python workshop Part 3 by Khiati Zakaria
# Exercise 1


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
n=int(input("Input a number to compute the factiorial : "))

print(factorial(n))