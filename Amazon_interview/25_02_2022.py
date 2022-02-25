#  python for recurretion

def func(val):
    if val>0:
        result = val + func(val-1)
        print(result)
    else:
        result = 0
    return result

print(func(6))


# febonice series in python with recurretion.

def febo(num):
    if num <=1:
        return num
    else:
        return febo(num-1) + febo(num-2)


#  factorial in python 

