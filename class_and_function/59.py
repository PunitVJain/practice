#  python with decorator .
#  decorator are the function which takes the function &
#  enhances the functionality of the existing function.

#  decorators start with "@" in python.
#  functions are the first class citisions.

# due to the functions are first class citisions in python.
# stack DS with python.










# rev string element with words

mystr = "Punit Vinod Jain"

myname = " ".join(mystr.split()[::-1])
# print(myname)



# check the string elements in list

mystr = "23451123asfoiywoeifvbh"
mylist = list(mystr)
print(mylist)
atozand0to9 = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
new_list = []
for iteam in atozand0to9:
    if iteam not in mylist:
        new_list.append(iteam)
print(sorted(new_list))

mylist = [ele for ele in atozand0to9 if ele not in mylist]

print(mylist)