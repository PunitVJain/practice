# Given a signed 32-bit integer x, 
# return x with its digits reversed. 
# If reversing x causes the value to 
# go outside the signed 32-bit integer 
# range [-231, 231 - 1], then return 0.

# Assume the environment does not allow 
# you to store 64-bit integers (signed or unsigned).
# Given a signed 32-bit integer x, return x 
# with its digits reversed. If reversing x 
# causes the value to go outside the signed 32-bit 
# integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you 
# to store 64-bit integers (signed or unsigned).
import math
class Solution:

    def reverse_num(self, num:int):
        if num >= pow(2,31) * -1 or num < (pow(2 ** 31) - 1):
            if num == 0: return 0
            elif num < 0:
                num = num * -1
                mod_num = str(num)
                new_num = int(mod_num[::-1])
                return new_num * -1
            else:
                mod_num = str(num)
                new_num = int(mod_num[::-1])
                return new_num
        else:
            return 0

if __name__ =="__main__":
    sol = Solution()
    print(sol.reverse_num(1534236469))