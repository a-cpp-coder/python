# the initial list comprehension can be any arbitary expression,
# including another list comprehension
# => nested list comprehension

# Example:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# similar to "flaten_a_list.py" example, but more clear how matrix is a list of lists
# need to go the outer loop 1st that is row (list of lists)

# transpose the the matrix
vec = [[row[i] for row in matrix] for i in range(0, 4)] # "for i in range(4)" is the most outter loop
print(vec)

# equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])   # append the list, each list made up from each row[i] in the matrix

print(transposed)

# more upack:
transposed = []
print(transposed)
for i in range(4):  # because each row has 3 elements
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)   # yes, append a list to a list then we will have list of lists

print(transposed) 