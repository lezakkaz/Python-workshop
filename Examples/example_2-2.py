# Python workshop Part 3 by Khiati Zakaria
# Example 2-2 (Functions)

# Create the function named helloWorld without any arguments and returns nothing
# to fix the error we had before, we will use the built in function of python named str(input)
# which changes the given input to a string

def helloWorld(x):
	print(str(x) + " Hello world!")


# Use a loop to call the above function 10 times while giving i as an input

for i in range(10):
	helloWorld(i)
