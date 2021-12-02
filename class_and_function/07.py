#  covert lists into dictionary.

mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def cdict(mylist1, mylist2):
    it1 = iter(mylist1)
    it2 = iter(mylist2)
    mydict = dict(zip(it1, it2))
    return mydict

print(cdict(mylist1, mylist2))


