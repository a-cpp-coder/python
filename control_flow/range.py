# I worry that I will forget

for i in range(0, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(25, 10, -96):
    print(i)

a = ["Truong", "Quang", "Huy"]
for i in range(len(a)):
    print(i, a[i])

for i, v in enumerate(a):       # the way to handle indices, straight forward, but your mind was too narrowed to see it
    print(i, v)

for i in list(range(len(a))):   # make a list from the range()-returned object(iterable), the list is more than iterable
    print(i, a[i])

# range(10) vs list(range(10))
# Later we will see more functions that return iterables and take iterables as argument.
