# basics of python.
print('Punit Jain.')

print('''My name is 'Punit Jain'. 
        I am from 'Malkapur'. 
        It's awesome working with 'PYTHON'.''')
name = 'Punit Jain' #  string variable.
print(f'My name is "{name}".')# f string.
print('My name is ', name) # just print.
print('Name is ' +name) # just print.
print('Name %s' %name)
print('*' * 100)
#------------------------------------------------------------------
print(type(name))

mylst  = [(10,20,30), (20, 30, 40),(50, 60, 90)]

print(list(filter(lambda ele: ele if ele[1]< 60 and ele[1] > 20 else None, mylst)))
# ===================================================================================


# dictionary comprehension
from math import pow
nums = [20, 23, 24, 25, 26, 18, 19]

mydict = {ele: pow(ele,2) for ele in nums}
print(mydict)