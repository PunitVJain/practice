# interview questions.
# equlibrium list.

# [1,7,3,6,5,6]

def eqidx(mylist):
    mylist = [iteam for iteam in range(len(mylist)) if sum(mylist[iteam+1:]) == sum(mylist[:iteam])]
    return mylist
mylist = [0, -7, 1, 5, 2, -4, 3, 0]

#print(eqidx(mylist))

def febio(rt):
    fv, sv = 0, 1
    while fv < rt:
        print(fv, end=' ')
        fv, sv = sv, fv + sv
    print()

rt = 5
#febio(rt)


#----------------------------------

def isbeautiful(N):
    nums = list(str(N))
    nums = list(map(int, nums))
    print(nums)
    mylist = []
    for iteam in range(len(nums)):
        if nums[iteam] == nums.count(nums[iteam]):
            mylist.append(True)
            #print(nums[iteam])
        else:
            #print(nums[iteam], nums.count(iteam))
            mylist.append(False)
    print(mylist)
    return all(mylist)

print(isbeautiful(333))


#-------------------------------------------------




N = 10
buildings = {buld:height for buld in range(1,N)}






