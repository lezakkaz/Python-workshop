# Python workshop Part 3 by Khiati Zakaria
# Example 6 (Functions)


def foo(x,y,z): 
    return(2*x,4*y,8*z)

a = foo(2,3,4)
print(a)

b = foo(z=4, y=2, x=3)
print(b)

c = foo(-2, z=-4, y=-3)
print(c)

# as you can see order doesnt really matter as long as the name of the arguments is given