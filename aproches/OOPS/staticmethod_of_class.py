# python

class MySample:

    @staticmethod
    def first_sample(val, ele):
        return val + ele
    
    @classmethod
    def second_sample(cls, first_name, last_name):
        return first_name +" "+last_name

    

ms = MySample()
print(ms.first_sample(4,5))    
print(MySample.first_sample(2,3))
print(ms.second_sample("Punit", "Jain"))
print(MySample.second_sample("Sam", "Jain"))
# static method does not take self, cls as argument
# normal methods takes self as first argument.
# classmethod takes instance of class as first argument
#  static method can be called with the instance of class

