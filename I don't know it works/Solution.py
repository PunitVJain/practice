#python list

mylist = [2, 3, 4, 2, 4, 65, 9]

print(id(mylist))
print(type(mylist))
#  when the value of the any list element is changed
# list reference is changed.

class SolutionSample():
    
    def __init__(self) -> None:
        pass

    def add_params(self):
        return "My Params"

class SolutionSampleone(SolutionSample):
    pass

solsam = SolutionSample()
print(solsam.add_params())