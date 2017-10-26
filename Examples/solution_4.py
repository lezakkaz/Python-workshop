# Python workshop Part 3 by Khiati Zakaria
# Exercise 4

def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("joke.txt"))


