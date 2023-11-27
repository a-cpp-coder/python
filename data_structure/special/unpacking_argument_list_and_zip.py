# to clear about * and zip()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(matrix)
print(*matrix)
print(*matrix[1])
c = list(zip(*matrix))
print(c)
# test = zip(*matrix[0])
# print(test)

# a_list = [1, 2, 3, 4]
# print(*a_list)
# b = zip(*a_list)
# print(b)

