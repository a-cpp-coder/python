# need to practice all

fruit = ["orange", "apple", "kiwi", "dragon fruit", "banana"]
print(fruit)

fruit.append("watermelon")
print(fruit)

fruit_2 = ["strawberry", "grape"]
fruit.extend(fruit_2)
print(fruit)

# fruit.insert(0, "pear")
fruit.insert(1, "pear")
print(fruit)

fruit.append("watermelon")
print(fruit)

fruit.remove("watermelon")  # remove the 1st item encountered from  the beginning
print(fruit)

while(fruit.count("watermelon") != 0):  
    fruit.remove("watermelon")
print(fruit)

fruit.pop(6)
print(fruit)

fruit.pop()
print(fruit)

tree = fruit            # like a reference
plant = fruit.copy()    # shallow copy but get own diff address

fruit.clear()
print(fruit)
print(len(fruit))
#print(fruit[0])

print(tree)
print(plant)

print(plant.index("kiwi"))
# print(plant.index("kiwi", 4))
print(plant.index("kiwi", 3, 7))

plant.sort()
print(plant)

plant.reverse()
print(plant)
plant.reverse()
print(plant)

plant.sort(reverse = True)
print(plant)
plant.sort(reverse = True)
print(plant)

plant.reverse()
print(plant\
      )





