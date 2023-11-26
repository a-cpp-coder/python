# more examples in list comprehension

vec = [i for i in range(-4, 4 + 1, 2)]
print(vec)

vec_2 = [x * 2 for x in vec]
print(vec_2)

vec_3 = [x for x in vec if x >= 0]
print(vec_3)

# apply a function to all elements in vec
vec_4 = [abs(x) for x in vec]
print(vec_4)

# call a method on each element 
fruit = [" apple", "orange    ", " passion fruit  " ]
fruit_strp = [f.strip() for f in fruit]
print(fruit_strp)

# create a list of 2-tuples like (number, square)
vec_5 = [(x, x**2) for x in (0, 5 + 1)]     # yeah, see how you are wrong
print(vec_5)

vec_5_correct = [(x, x**2) for x in range(0, 5 + 1)]    # need range() function
print(vec_5_correct)                                    # and also the tuple must be parenthesized, yeah, that's how a tuple

