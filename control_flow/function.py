# a fibonacci to understand how to write functions in Python
# print the first n number of of Fibonacci sequence

# loop ver
def Fibo(n):                # the keyword def use to indicate a function definition, followed by function name, and formal parameters
    a, b = 1, 0
    i = 0
    while(i < n):
        print(a, end = " ")
        i = i + 1
        a, b = a + b, a
        pass

n = int(input("Write an integer number: "))  
Fibo(n)
print()

# recursion ver
def Fibo_2(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return Fibo_2(n - 1) + Fibo_2(n - 2)
    pass

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(Fibo_2(i), end = "")
print()

# math ver
# we have exact formula for calculating Fibo numbers
