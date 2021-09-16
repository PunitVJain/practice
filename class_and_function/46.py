# leetcode problems:
# Python.

mylist = [[10, 20, 30, 40],[20, 30, 40, 50],[60, 70, 80, 90],[100, 120, 130, 20],[30, 40, 50]]
print(sorted(mylist, key= lambda iteam: iteam[-1]))

def rev_str(mystr):
    return ' '.join(mystr.split()[::-1])

mystr = "Punit Vinod Jain"
print(rev_str(mystr))