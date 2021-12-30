# generator in python.

def mygenerator():
    for iteam in range(100):
        yield iteam
#x = mygenerator()

#  as in python needed to use __next__()
#  if there is yield in function this will be generator.

def samgenerator():
    co = 0
    while True:
        co += 1
        yield co
print(samgenerator().__next__())
print(samgenerator().__next__())
print(samgenerator().__next__())
print(samgenerator().__next__())
print(samgenerator().__next__())
print(samgenerator().__next__())