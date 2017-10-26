# Python workshop Part 3 by Khiati Zakaria
# Exercise 2

def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total 
    
print(multiply((8, 2, 3, -1, 7)))