#  python 

#  connect pythom code with java code.

# OR write the python code same as that of the JAVA code.

# py4j will initiate jvm to access in python code.

#from py4j.java_gateway import JavaGateway

#obj = JavaGateway()


class Sample:

    myself = "Malkapur"

    def __init__(self, name) -> None:
        self.name = name
    

class Example(Sample):

    def __init__(self, name) -> None:
        super().__init__(name)

ex = Example("Maharashtra")
print(ex.myself)        