# a good way to doc

def func_1(n):
    """
        This is a doc string

        it does nothing
    """

print(func_1.__doc__)

def f(ham: str, eggs: str = 'eggs') -> str:
    pass
print("Annotations:", f.__annotations__)