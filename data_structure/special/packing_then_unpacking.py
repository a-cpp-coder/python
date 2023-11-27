# the way of doing it

def func1(a, b, c):
    print(a, b, c)

def func2(*args):
    a_list = list(args)     # convert args tuple to list so that I can modify it

    # Modifying args
    # args[0] = "I"           # Ngao
    # args[1] = "am"          # Tuple is immutable
    a_list[0] = "I"
    a_list[1] = "am"

    # Unpacking again to pass it to func1
    func1(*a_list)

func2("Truong", "Quang", "Huy")