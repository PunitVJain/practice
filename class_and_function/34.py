# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 8, 2, 7, 3, 6, 4, 5]

def fun_sort_list(mylist):
    ft = 0
    lt = -1
    new_list = []
    for iteam in range(0, round(len(mylist)/2)):
        if mylist[ft] != mylist[lt]:
            new_list.append(mylist[ft])
            new_list.append(mylist[lt])
        ft += 1
        lt -= 1
    return new_list

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(fun_sort_list(mylist))