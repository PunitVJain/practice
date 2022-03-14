#  Leet code Question.

class Solution:

    def func(self, mystr:str):   
        mynum = ''
        for iteam in mystr:
            if iteam.isdigit():
                mynum = mynum + iteam
        return int(mynum)

sol  = Solution()
print(sol.func())
#  ------------------------------


class Sample:

    def __init__(self) -> None:
        pass
    
    def name(self):
        return "Punit Jain"