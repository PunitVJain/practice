#  python for recurretion

def func(val):
    if val>0:
        result = val + func(val-1)
        print(result)
    else:
        result = 0
    return result

#print(func(6))


# febonice series in python with recurretion.

def febo(num):
    if num <=1:
        return num
    else:
        return febo(num-1) + febo(num-2)


#  factorial in python 

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)
    
print(fact(4))

# ------------------------------------
# Recurresion involves calling  the function inside the function 
# with the base condition

def myfunc(item):
    # recursive function.
    if item <=0:
        #  base condition.
        return 1
        # function calling itself in function.
    return item + myfunc(item-1)