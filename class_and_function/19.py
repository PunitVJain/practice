#  Python start - 21-07-2021

# You are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.

mylist1 = [2,4,3]
mylist2 = [5,6,4]

def add_element(mylist1, mylist2):
    sum_list = []
    if len(mylist1) == len(mylist2):
        for iteam in range(0, len(mylist2)):
            add = mylist1[iteam] + mylist2[iteam]
            sum_list.append(add)
    return sum_list
#print(add_element(mylist2, mylist1))

if __name__ == '__main__':
    print(add_element(mylist1, mylist2))
    #print(__name__)



