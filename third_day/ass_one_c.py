#  single inheritance in python.

class SampleOne:
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    

class SampleTwo(SampleOne):

    def __init__(self, first_name, middle_name, last_name):
        self.middle_name = middle_name
        super().__init__(first_name, last_name)
    
    def full_name(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

if __name__ == "__main__":
    sam = SampleTwo("Punit", "Vinod", "Jain")
    print(sam.full_name())

# single inheritance in python with super() & instance of the class.
