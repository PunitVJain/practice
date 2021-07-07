# leet code Q2




mylist1 = [2,4,3]
mylist2 = [5,6,4]

def add_ele(mylist1, mylist2):
    it = iter(mylist1)
    rt = iter(mylist2)
    sum_of = []
    sum = lambda it, rt: it + rt
    sum_of.append(sum)
    return sum_of

print(add_ele(mylist1, mylist2))