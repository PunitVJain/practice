#  python developer.

def fun_sort(mylist):
    return sorted(mylist, key= lambda sec_ele: sec_ele[-1])

mylist = [[10,20,90],[30, 40, 60],[20, 40, 10],[20, 30, 50]]
print(fun_sort(mylist))