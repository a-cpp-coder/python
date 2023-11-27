# to understand key:value in dictionary data structure

def func(** kwargs):
    print(type(kwargs))

    # print dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))

# Driver Code
func(name = "Huy", ID = "25")  # pass a dictionary