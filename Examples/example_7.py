# Python workshop Part 3 by Khiati Zakaria
# Example 7 (Functions)

# same as example 6, order does not matter when the valuse are named
# if not then the comiler will think that, the values given are already in order

def foo(x=1,y=2,z=3): 
	return(2*x,4*y,8*z)

a = foo()
print(a)

b = foo(z=100)
print(b)

c = foo(200)
print(c)


