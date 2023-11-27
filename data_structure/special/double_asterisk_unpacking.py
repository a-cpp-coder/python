# double asterisk is used for unpacking dictionaries

a_dictionary = {"a":2, "b":3, "c":4 }

def func(a, b, c):
    return a + b + c

# Driver
print(func(*a_dictionary))
print(func(**a_dictionary))
