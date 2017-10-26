# Python workshop Part 3 by Khiati Zakaria
# Example 2-1 (Functions)

# Create the function named helloWorld without any arguments and returns nothing
# it is suppose to print a number before it prints hello world! 
# for exampe, if your input is helloWorld(5) it should print 5 Hello world!

def helloWorld(x):
	print(x + " Hello world!")


# Use a loop to call the above function 10 times while giving i as an input

for i in range(10):
	helloWorld(i)


# if you try to run this, the compiler will return an error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# and that is because you can't add an integer to a string