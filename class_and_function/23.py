# leet code : 03
# Given a string s, 
# find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        current_length = 0
        start_index = 0
        max_length = 0

        for i, c in enumerate(s):
            if c in seen and seen[c] >= start_index:
                start_index = seen[c] + 1
            seen[c] = i

            current_length = i - start_index + 1
            if current_length > max_length:
                max_length = current_length

        return max_length

sam = Solution()

class Solution:
    def len_of_lon_sub_str(self, s: str) -> int:
        checked = dict() #  dictionary for the elements to be added
        start_index = 0 # start index of the longest length
        curr_index = 0 #
        curr_len = 0


























