#  leet code question

# You are given a positive integer num 
# consisting only of digits 6 and 9.
# Return the maximum number you can get 
# by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        sum = []
        for iteam in range(len(nums)):
            if nums[iteam] == '6':
                nums.replace(nums[iteam], '9') 
                sum.append(nums)
                
            elif nums[iteam] == '9':
                nums.replace(nums[iteam], '6')
                sum.append(nums)
        sum = list(map(int, sum))
        print(sum)
        return max(sum)
        
sol = Solution()
print(sol.maximum69Number(9669))