# generator in python.

def mygenerator():
    for iteam in range(100):
        yield iteam
x = mygenerator()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
#  as in python needed to use __next__()
#  if there is yield in function this will be generator.

