# write a function to get febonicy list elements.

class Solution:
    def sumele(self, nums:list):
        return [sum(nums[:ele + 1]) for ele in range(len(nums))]


if __name__ == "__main__":
    sol = Solution()
    lst = [10, 20, 30, 40, 50]
    print(sol.sumele(lst))