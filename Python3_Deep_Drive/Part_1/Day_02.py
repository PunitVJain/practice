#  python 
import collections
var3=['red', 'blue', 'orange','red','yellow','orange', 'red','white', 'black','pink','red','white','blue']
# print(collections.Counter(var3))


def func(mylst):
    mylet = set(mylst)
    mycount = dict()
    for iteam in mylet:
        mycount[iteam] = mylst.count(iteam)
    return mycount

print(func(var3))
# -------------------------------
# print the common elements in the below list in optimal way
list_1= [(4,),(5,),(6,),(7,)]
list_2 = [(3,),(6,),(5,),(7,)]

def com(mylst1, mylst2):
    common = []
    for iteam in mylst1:
        if iteam in mylst2:
            common.append(iteam)
    return common

print(com(list_1, list_2))
# ---------------------------

# using list comphrehension, 
# print list of all the even number from 0 to 20 and 
# multiply each even number with 2.

mylst = [ele*2 for ele in range(0,21) if ele%2==0]
print(mylst)

list1= ['w','e','l','c','o','m','e']
#result =''
#for c in list1:
#    result = result+c
#print(result)
print(''.join(list1))
# -------------------------------------------


#rewrite the following code in optimized way
a=1
b=2
#temp = a
#a=b
#b=temp
#print(a,b)
print("Values before swap: ", a,b)
a, b = b, a
print("Values after swap: ", a, b)
# Write a Python program to produce Star triangle

#for item in range(0,5):
   # print(item * '*')

print('\n'.join([ele* '*' for ele in range(0,5)]))
# ---------------------------------------------------------------------------
# rewrite the following code in optimized way
week={}
week['sun']=0
week['mon']=1
week['tue']=2
week['wed']=3
week['thu']=4
week['fri']=5
week['sat']=6



for key, value in week.items():
    if value%2==0:
        print(key, ":Even")
    else:
        print(key, ":Odd")


# ---------------------------------------------------------

#write a program in all possible ways to get the value of  mark from a dictionary
student={"name":"Tom", "class":8, "mark":75}
print(student["mark"])
print(student.get("mark"))
# -------------------------------