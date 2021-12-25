# decorators in python





def decore(func):
    def wrapper(*args, **kwargs):
        return "My new function is " + func()
    return wrapper


@decore
def name():
    return "Punit Jain"


#print(name())


# -----------------------------------------------------------------------




def even_decore(func):
    def wrapper(*args, **kwargs):
        return list(filter(lambda ele: ele if ele % 2 == 0 else None, func()))
    return wrapper

@even_decore
def nums():
    return [ele for ele in range(1, 101)]


#print(nums())

# ================================================================================


def decorator_func(func):
    def wrapper(*args, **kwargs):
        return  func() * 2
    return wrapper

@decorator_func
def name_func():
    return "Punit "

#print(name_func())

# =============================================================
def evendecore(func):
    def wraapper(*args, **kwargs):
        if func().__next__() % 2 == 0:
            return func().__next__()
        return None
    return wraapper



@evendecore
def series_nums():
    try:
        for iteam in range(1, 100):
            yield iteam
    except:
        yield None
        
# this is not possible with python to keepp generato function as 

print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())
print(series_nums().__next__())



    