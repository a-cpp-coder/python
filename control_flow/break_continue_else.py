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
# normally, you will need a flag to keep track of the divisability of i but with for loop's else (try's taste)
# you dont need that

# When used with a loop, the else clause has more in common with the else clause of a try statement than it
# does that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else
# clause runs when no break occurs.

