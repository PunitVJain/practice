# input as list 
def input_arr():
    arr = input()
    arr = tuple(map(str, arr.split()))
    return arr
print(input_arr())