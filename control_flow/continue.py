# thanh tinh

# print odd and even number

n = 10
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "is an even number")
        continue
    print(i, "is an odd number")

# or just if/else

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "even number")
    else:
        print(i, "odd number")