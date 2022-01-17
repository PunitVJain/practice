# classes in python.

# Diagonal inheritance

class SampleOne:

    value_one = "Indian"

    def __init__(self, value_two) -> None:
        self.value_two = value_two


class SampleTwo(SampleOne):

    def __init__(self, value_two, value_three) -> None:
        super().__init__(value_two)
        self.value_three = value_three
    
    def add_values(self):
        return self.value_one + self.value_two + self.value_three
    
class SampleThree(SampleOne):

    def __init__(self, value_two, value_four) -> None:
        super().__init__(value_two)
        self.value_four = value_four

class SampleFour(SampleThree):

    def __init__(self, value_two, value_four) -> None:
        super().__init__(value_two, value_four)

sam_four = SampleFour("Punit", "Jain")
print(sam_four.value_one, end="")

class ExampleOne():
    def __init__(self) -> None:
        pass