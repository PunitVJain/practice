class Sample:
    def __init__(self) -> None:
        pass
    def add(self):
        return "Add from Sample"

class MoreSample(Sample):
    def add(self):
        return "Add from MoreSample"

class AgainSample(MoreSample):
    def something(self):
        return "Something", super(Sample)


if __name__ == "__main__":
    sam = AgainSample()
    print(AgainSample.mro())

