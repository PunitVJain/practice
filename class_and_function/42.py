#  python .

mylist = [20, 30, 50, 60, 10]
val = int(input("Enter the value to be replaced: "))

def func_add(mylist):
    mylist  = list(map(lambda iteam: iteam if iteam != val else "_", mylist))
    return mylist

print(func_add(mylist))

