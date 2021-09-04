#  python developer.

# Write a function to find the longest common prefix 
# string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0: return ""
        elif len(strs) == 1: return strs[0]
        min_s = min(strs, key= len)
        max_s = max(strs, key= len)
        for iteam, value in enumerate(min_s):
            if max_s[iteam] != value: 
                return min_s[:iteam]
        return min_s

so = Solution()
mystr = ["Vimal"]
print(so.longestCommonPrefix(mystr))


