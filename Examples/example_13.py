# Python workshop Part 3 by Khiati Zakaria
# Example 13 (Files I/O)


# open the file named joke1.txt for reading only
file = open('joke.txt', 'r')

# loop over the lines in the text file and then print each line
for line in file:
    print(line)

# close the file
file.close()


