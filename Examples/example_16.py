# Python workshop Part 3 by Khiati Zakaria
# Example 16 (Exceptions)

import sys

while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")
         sys.exit(1)

print("The number was", x)
