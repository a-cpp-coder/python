# A list comprehension
# consist of brackets
# containing an expression
# follow by a "for" clause,
# then zero or more "for" or "if" clause

list_1 = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]   # (x, y) is a tuple, like (x, y, z)
print(list_1)
print(type(list_1[0]))

result = []
# equal to
for x in [1, 2, 3]:
    for y in [3, 4, 5]:
        if x != y:
            result.append((x, y))

print(result)

# note the order of "for" clauses and "if" clauses is the same in both examples
