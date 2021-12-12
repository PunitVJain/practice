# decorators in python



from importlib_metadata import re


def decore(func):
    def wrapper(*args, **kwargs):
        return "My new function is " + func()
    return wrapper


@decore
def name():
    return "Punit Jain"


print(name())


# -----------------------------------------------------------------------




def even_decore(func):
    def wrapper(*args, **kwargs):
        return list(filter(lambda ele: ele if ele % 2 == 0 else None, func()))
    return wrapper

@even_decore
def nums():
    return [ele for ele in range(1, 101)]


print(nums())

# ================================================================================


