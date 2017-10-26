# Python workshop Part 3 by Khiati Zakaria
# Example 10 (lambda)

def add1(x): return x+1
def odd(x): return x%2 == 1
def add(x,y): return x + y

a = map(add1, [1,2,3,4])
print(a)

#b = map(+,[1,2,3,4],[100,200,300,400])
#print(b)

c = map(add,[1,2,3,4],[100,200,300,400])
print(c)

e = filter(odd, [1,2,3,4])
print(e)
