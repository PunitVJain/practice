#  python class 

class Example:

    pass


mylst =  []
print(id(mylst))
mylst.append('Punit Jain')
print(id(mylst))
print(mylst)


class SampleSolution:
     
    def __init__(self, name) -> None:
        self.name = name

    def name_add(self):
        return "Punit Jain from SampleSolution"

class SampleSolutionOne:

    def __init__(self, name) -> None:
        self.name = name

    def name_add(self):
        return "Punit Jain from SampleSolutionOne"

class SampleSolutionTwo:

    def __init__(self, name) -> None:
        self.name = name

    def name_add(self):
        return "Punit Jain from SampleSolutionTwo"


class SampleSolutionAll(SampleSolution, SampleSolutionOne, SampleSolutionTwo):

    def __init__(self) -> None:
        super(SampleSolutionOne).__init__()
ssa = SampleSolutionAll()
print(super(SampleSolutionOne, ssa).name_add())