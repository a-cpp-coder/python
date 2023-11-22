words = ["abc", "def", "ghij"]
i = 0

# modify the *mutable sequence directly in loop leads to unspecified behavior
# for w in words:                 
#     if(len(w) > 3):
#         words.insert(0, w) 
#         i = i + 1
#         print(w, i)

# make a copy to modify
for w in words[:]:
    if(len(w) > 3):
        words.insert(0, w) 
        i = i + 1
    print(w, i)

for w in words:
    print(w)
    