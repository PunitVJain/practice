#  python for me .
#  find the even numbers from the list
#  simple with lambda function.




mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = list(filter(lambda num: num %2 == 0, mylist))

#print(even_list)

# =======================================================

#  generators in python.

#  write a febonici series with the help of generators.

#===================================================

# febo




def febo(limit):
    val, ele = 0, 1
    while val < limit:
        yield val
        val, ele = ele, val + ele

value = febo(10)

print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())
print(value.__next__())

