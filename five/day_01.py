#  python magic methods.

def myfunc():
    a = "Jain"
    b = "Malkapur"
    return "Punit Jain"

print(myfunc.__class__)
print(myfunc.__code__.co_consts)