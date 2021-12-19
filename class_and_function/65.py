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

def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
  
# Create a generator object
x = fib(5)
  
# Iterating over the generator object using next
print(x.__next__()) # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
     
