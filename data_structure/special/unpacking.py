# Background

def func(a, b, c, d):
    print(a + b + c +d)

my_list = [1, 2, 3, 4]
# func(my_list)               # can't excute because my_list is just 1 object but func requires 4

# Unpacking a list
func(*my_list)

# the No. Elements must match the No. formal parameters
# other example
my_list2 = [0, 6]
print(range(*my_list2))     # abstract like eval()
my_list3 = [6]
print(range(*my_list3))
