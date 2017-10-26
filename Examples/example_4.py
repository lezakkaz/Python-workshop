# Python workshop Part 3 by Khiati Zakaria
# Example 4 (Functions)

# a function that returns nothing and prints Hello world!

def helloWorld():
	print("Hello world!")

 
x=helloWorld()
print(x)

# As you can see when you run this code two things are printed
# first thing printed is Hello world! because we called helloWorld() in x = helloWorld()
# and since helloWorld() returns nothing, in other words None, x = None, so print(x) will print None