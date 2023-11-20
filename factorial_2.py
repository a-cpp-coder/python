def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("Enter a number: ")) # function is an object
while num >= 1:
    print(factorial(num))           # function is an object 2
    num = num - 1
