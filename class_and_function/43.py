# python.
mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def func_sort(mylist):
    ft = 0
    lt = -1
    modlist = []
    for _ in range(round((len(mylist))/2)):
        modlist.append(mylist[ft])
        modlist.append(mylist[lt])
        ft += 1
        lt -= 1
    return modlist

print(func_sort(mylist))
