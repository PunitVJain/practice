#  python function.

mystr = 'My name is Punit Jain'

# O/p = 'A IDNI evolI'


def revspace(mystr):
    index_No = [] # index number of the space
    for iteam, value in enumerate(mystr):
        if value == ' ':
            index_No.append(iteam)
    mstr = mystr.replace(' ', '') # replaces the ' ' 
    revstr = list(mstr[::-1]) # reverse the string & converted to list
    for ind in range(len(index_No)):
        revstr.insert(index_No[ind], ' ') # inserted the space at the index_no list elements
    revstr = ''.join(revstr) # join & converted to string
    return revstr
print(revspace(mystr))


# reverse the string without predefined functions & slicing.

def reverse_string(mystr):
    index = len(mystr)
    mylist = []
    while index:
        index -= 1
        mylist.append(mystr[index])
    return ''.join(mylist)
mystr = 'PunitJain'

print(reverse_string(mystr))



