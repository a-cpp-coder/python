# what is needed some times

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]     # a nested list - still a list, but some times, you need it to be flattened
print(vec)
print(type(vec))    

vec_flatten = [num for elemement in vec for num in elemement]
print(vec_flatten)
