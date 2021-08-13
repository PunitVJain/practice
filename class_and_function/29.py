#   filter function in python.

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even =  tuple(filter(lambda num :num%2==0, mylist))
print(even)

#  syntax of filter is
#  filter(function, iterables)
odd = tuple(filter(lambda num: num%2!=0, mylist))
print(odd)

double  = tuple(map(lambda num: num **2, mylist))
print(double)
