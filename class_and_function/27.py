class Solution:


	def lengthOfLongestSubstring(self, s: str) -> int:

		substring = ''
		max_ = 0
		for char in s:
			if char in substring:
				substring = substring.split(char)[1]
			substring += char
			max_ = len(substring) if len(substring) > max_ else max_
		return max_
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
# a --> ss --> a -->  


# "abcabcbb" -->  