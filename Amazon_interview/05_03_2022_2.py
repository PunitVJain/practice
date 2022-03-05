#  class in python for link list.

class ExampleOne:

    def __init__(self) -> None:
        pass

class ExampleTwo:

    def __init__(self) -> None:
        pass

class Example:

    def __init__(self, value_one, value_two) -> None:
        self.value_one = value_one
        self.value_two = value_two
    
    def add(self):
        return self.value_two + self.value_one
    
    def sub(self):
        return self.value_one - self.value_two

    def mul(self):
        return self.value_two * self.value_one

    def div(self):
        try:
            return self.value_one // self.value_two
        except:
            return "Invalid Numbers"

if __name__ == "__main__":
    ex = Example(3, 2)
    print(ex.add())
    print(ex.sub())
    print(ex.mul())
    print(ex.div())

    