#  classes in python.
#  best practice to code with python OOP.

class Apple(object):

    def __init__(self) -> None:
        super().__init__()
    
    def add_two_numbers(self, num_one, num_two):
        return num_one + num_two
    
    def main(self):
        app_one = Apple()
        first_num  = int(input("Enter the first value: "))
        second_num = int(input("Enter the second value: "))
        print(f"The Addition of the two numbes {first_num} & {second_num} is:",app_one.add_two_numbers(first_num, second_num))

#if __name__ == "__main__":
    #app_two = Apple()
    #app_two.main()
#  ================================================================================
#  MRO in Python.
#  Method Resolution Order
#  

class SampleMade(object):

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    
sm = SampleMade("name")
print(sm.__dict__)
