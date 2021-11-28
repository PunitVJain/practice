#  decorators in python
#  needed to create decorator as before name it must return 'My name is'.
#  example of decorators.

def decfun(name):
    def wrapper(*args, **kwargs):
        return "My name is " + name()
    return wrapper

@decfun
def name():
    return 'Punit Jain'

print(name())

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]

even_num_list = list(filter(lambda ele: ele % 2 == 0, mylist))
print(even_num_list)