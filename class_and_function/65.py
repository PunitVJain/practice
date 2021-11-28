#  python for me .
#  find the even numbers from the list
#  simple with lambda function.

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = list(filter(lambda num: num %2 == 0, mylist))

print(even_list)

