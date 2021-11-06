#  decorators in python
# needed to create decorator as before name it must return 'My name is'.
#  example of decorators.

def decfun(name):
    def wrapper(*args, **kwargs):
        return "My name is " + name()
    return wrapper

@decfun
def name():
    return 'Punit Jain'

print(name())