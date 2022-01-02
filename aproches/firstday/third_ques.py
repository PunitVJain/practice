class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        srt = s.split(" ")
        srt = list(map(lambda ele: ele.strip(), srt))
        srt = list(filter(lambda ele: ele if ele != " " else None, srt))
        return len(srt[-1])
sol = Solution()
print(sol.lengthOfLastWord(s = "   fly me   to   the moon  "))
