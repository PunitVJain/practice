#  class variables & instance variables.

class SampleOne:

    num = 10 
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name # instance variable in python
        self.last_name = last_name # instance variable in python
        
    def full_name(self):
        return self.first_name + " " + self.last_name, self.num


        

sam_one = SampleOne("Punit", "Jain")
sam_two = SampleOne("Geeta", "Jain")
sam_three = SampleOne("Ram", "Jain")
sam_four = SampleOne("Seeta", "Jain")
sam_five = SampleOne("Lakshaman", "Jain")
sam_six = SampleOne("Hanuman", "Jain")
sam_seven = SampleOne("Ravan", "Jain")
#print(sam_one.first_name)
print(sam_one.num) # can access the class variable with class & instance of the class out side the class
print(SampleOne.num) 
print(sam_one.first_name)

print(sam_one.full_name())
print(sam_two.first_name)
print(sam_two.full_name()) #  class variable & instance variable can be access with self inside the class
print(sam_one.__dict__)
print(sam_two.__dict__)
print(SampleOne.__dict__)
print(sam_one.__new__(SampleOne))



# instance variables are the variables defined in constructor of the class.
# instance variable create the copy for the each object.
# if the changes made in one copy will not reflect in other copes of the instance variable.
# instance variables can be accessed in class with self keyword & outside the class they can be accessed by object name
# The method who access the instance variable is called instance method.


