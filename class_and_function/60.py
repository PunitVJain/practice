# leet code questions
# Febonici series in generator.

# febo




def febo(limit):
    val, ele = 0, 1
    while val < limit:
        yield val
        val, ele = ele, val + ele

value = febo(10)

#print(value.__next__())
#print(value.__next__())
#print(value.__next__())
#print(value.__next__())
#print(value.__next__())

#======================

# normal function with febonicie.

def febonic(lim):
    val, ele =  0, 1
    while val < lim:
        print(val, end=" ")
        val, ele = ele, val + ele

febonic(10)

