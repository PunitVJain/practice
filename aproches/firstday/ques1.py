#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

from inspect import stack


class Solution:

    def isValid(self, mstr:str):
        mstack, mdict = [], {'(':')','{':'}', '[':']'}
        for ele in mstr:
            if ele in mdict:
                mstack.append(ele)
            elif not mstack or mdict[mstack.pop()] != ele: return False
        return not mstack


sol = Solution()
print(sol.isValid("((())()()()()"))
