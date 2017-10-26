# Python workshop Part 3 by Khiati Zakaria
# Example 11 (modules)


# Import a library named numpy, but to make it short we can just call it np or whatever suits you
import numpy as np

# to avoid importing the whole library to the memory, we can just import the functions that we need
from math import log2, log10, sqrt

# We can also just import anything in the library this way too,
from random import *

import random

import sys

# numpy.zeros creates an empty matrix with zeros of the given size
matrix = np.zeros((3,4))
print(matrix)

# logarithm base 2
a = log2(10)
print(a)

# square root
b = sqrt(81)
print(b)

# random integer between 1 and 10
c = randint(1,10)
print(c)

# split function splits a string to a list using spaces, if an argument is given then it will split using that char
deck = 'ace two three four'.split()
shuffle(deck)
print(deck)

# stops the algorithm with a 0 signal
sys.exit(0)

# this message will not be executed because sys.exit(0) stoped the algorithm
print("so sad! no one cares about me")