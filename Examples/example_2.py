# Python workshop Part 3 by Khiati Zakaria
# Example 2-2 (Functions)

# Create the function named helloWorld without any arguments and returns nothing
# all it does is print Hello world!
def helloWorld(x):
	print(str(x) + " Hello world!")


# Use a loop to call the above function 10 times
for i in range(10):
	helloWorld(i)
