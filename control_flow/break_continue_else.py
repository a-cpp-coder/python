# Prime Number in Python

n = 30

for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            print(i, "is not a Prime Number")
            break
    else:
        print(i, "is a Prime Number")
        # continue
    