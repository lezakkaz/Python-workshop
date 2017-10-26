# Python workshop Part 3 by Khiati Zakaria
# Example 5 (Functions)


# a function that takes 3 arguments, only a needs to be assigned, but b and c dont need to be given because they have a default value

def myfun(a, b=3, c="hello"):	
    return a + b


a = myfun(5,3,"hello")
print(a)

b = myfun(5,3)
print(b)

c = myfun(5)
print(c)

# all these previous calls return 8 
# because first call and second call they were both given 5 and 3 which adds to 8
# as for the third call, only a is given as 5, where b is equal to 3 by default
# c argument doesnt matter if its given or not because it is not used inside the function anyway

d = myfun(6,6,"Hi")
print(d)

# for the forth call, b was given as 6 and a as 6 and thus, the myfun function returns 12