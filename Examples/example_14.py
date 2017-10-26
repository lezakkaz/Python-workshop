# Python workshop Part 3 by Khiati Zakaria
# Example 14 (Files I/O)

file = open('new.txt', 'w')

file.write('line 1\n')
print('line 2', file=file)

file.close()
