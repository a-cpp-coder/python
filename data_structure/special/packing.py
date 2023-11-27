# When
# we dont know how many arguments need to be passed to a python funcion,
# we can use "packing" to pack all arguments in a tuple

def my_sum(*arg):
    return sum(arg)
# arg is a packed variable here <=>  a normal tuple
# arg[0], arg[1] will give you 1st and 2nd argument
# tuples are immutable then we need convert it to list so you can mutate it (modify, delete, re-arrange items with i)

# Driver Code
print(my_sum(1, 2, 3, 4))
print(my_sum(1, 2, 3, 4, 5))

# test tuple
def my_sum_2(a, b, c, d):
    return a + b + c + d

# Driver
a_tuple = (1, 2, 3, 4)
print(my_sum(*a_tuple))
print(my_sum_2(*a_tuple))
print(my_sum_2(a_tuple))