# Python workshop Part 3 by Khiati Zakaria
# Example 8 (Functions)


# a function can be called by another function or given as a argument

def square(x): 
	return x * x

def add(x):
    return x + x
    
def applier_1(q, x): 
	return q(x)
 
def applier_2(x):
    return square(x)

a = applier_1(square, 7)
print(a)

b = applier_1(add , 7)
print(b)

c = applier_2(7)
print(c)