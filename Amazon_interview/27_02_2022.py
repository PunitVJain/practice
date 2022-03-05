# python for Punit Jain
#  multi level inheritance in Python.

class First_Example:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
class Second_Example(First_Example):

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
    
    def full_name(self):
        return super().full_name() + ' '+ "This is from Second_Example."

class Example(Second_Example):
    pass


ex = Example('Punit', 'Jain')
print(First_Example.full_name(ex))   
print(Second_Example.full_name(ex))
#-------------------------------------------------

#  DFS & BFS graph traversal methods.



