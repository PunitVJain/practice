# interview questions.
# equlibrium list.

# [1,7,3,6,5,6]

def eqidx(mylist):
    mylist = [iteam for iteam in range(len(mylist)) if sum(mylist[iteam+1:]) == sum(mylist[:iteam])]
    return mylist
mylist = [0, -7, 1, 5, 2, -4, 3, 0]

print(eqidx(mylist))

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(10)