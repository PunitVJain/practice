# Given an integer array nums and an integer val, 
# remove all occurrences of val in nums in-place. 
# The relative order of the elements may be changed.



mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 50, 20]
val = 20
def func_rep(mylist, val):
    mylist  = list(map(lambda iteam : iteam if iteam !=val else "_", mylist))
    number_of_elements_replaced = mylist.count("_")
    return number_of_elements_replaced, 

print(func_rep(mylist, val))
