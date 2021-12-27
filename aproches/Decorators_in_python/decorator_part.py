#  decorators in python.

def evendecore(func):
    def wrapper():
        return list(filter(lambda ele: ele if ele % 2 == 0 else None, func()))
    return wrapper

@evendecore
def nums():
    return [ele for ele in range(1, 101)]

#print(nums())


# ==============================================================================

def divbythree(func):
    def wrapper():
        return list(filter(lambda ele: ele if ele % 3 == 0 else None, func()))
    return wrapper

@divbythree
def numbs():
    return [ele for ele in range(1, 101)]


print(numbs())