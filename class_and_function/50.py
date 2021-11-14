#A distinct string is a string that is present only once in an array.

#Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

#Note that the strings are considered in the order in which they appear in the array.

from typing import List


class Solution:

    def diststr(self, arr:List[str], k:int):
        mylist = []
        for iteam in range(len(arr)):
            if arr.count(arr[iteam])==1:
                mylist.append(arr[iteam])
        if len(mylist)==len(arr):
            return mylist[k-1]
        elif len(mylist)<k:
            return ""
        elif len(mylist)>=k:
            return mylist[k-1]
        



s = Solution()
arr = ["a","b","a"]
k = 3
print(s.diststr(arr, k))   

#arr = ["jqrd","k","miy","svuwg","uv","yttn","bxu","nymzu","dpane","x",
#"mb","zm","ae","ihwtn","kouej","y","zt","h","udx","h","imi",
#"zombs","l","hvt","uor","kzi","tzm","kde","ml","hmvz","hriuy",
#"lav","hlvw","fnnj","bdkh","hu","tuuob","uc","no","qo","ku","foe"]
#k = 27
#print(s.diststr(arr, k))
