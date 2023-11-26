# A Concise (and Incredible) way to create a Lists

# Normally, 2 ways to create a List (array/vector in advanced):

# Way 1: each member is a result of some operations applied to members of another list/iterable
list_1 = list("Way to creat a List from a String and remove all spaces".split(" "))
print(list_1)

list_2 = list_1.sort() # careful here, the sort() does the work, sorting all Strings in list_1 (be careful, need key here because we have upper cases character that have lower ASCII values) 
print(list_2)          # but it does not return a mutated sequence, it return a None Object, then list_2 is [] 
print(list_1)          

list_2 = sorted(list_1, reverse = True) # then you need to use a function like that to return a Mutated Object
print(list_2)

list_2 = sorted(list_1, key=str.lower, reverse = False) # Sorting with ignoring Case
print(list_2)
list_2 = sorted(list_1, key=str.upper, reverse = False) # Sorting with ignoring Case
print(list_2)

# Way 2: Create a sequence of elements that satisfy a certain condition

# List of Squares
list_3 = []
for i in range(0, 10 + 1):
    list_3.append(i ** 2)

print(list_3)

# List of Prime Numbers
list_4 = []
n = 10 ** 4
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break;
    else:
        list_4.append(i)

print(list_4)
x = 16
print(list_4[x - 1])
        