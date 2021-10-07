# input as list 
def input_arr():
    arr = input()
    arr = list(map(str, arr.split()))
    return arr
print(input_arr())