#  start with classes in python.
#  this is the bad way for the finding the addition of two numbers is even or not,
#  but to understand the concept of class method, can use this structure.
class Sample:
    @classmethod
    # if this method is not static method then it will give an error as one argument missing.
    # as the method is called with the class name
    def add(self, first_number:int, second_number:int):
        return first_number + second_number
#  python 

class Example(Sample):
    @classmethod
    # if this method is not static method then it will give an error as one argument missing.
    # as the method is called with the class name
    def check_addition_iseven(self,first_number:int,second_number:int):
        if Sample.add(first_number,second_number) % 2 == 0:
            return True
        return False


#print(Example.check_addition_iseven(2,3))
# =============================================================================

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]

even_num_list = list(filter(lambda ele: ele % 2 == 0, mylist))
print(even_num_list)





