class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedChars = set()
        l = 0
        longestSubstringSize = 0

        for r in range(len(s)):
            char = s[r]
            while char in visitedChars:
                visitedChars.remove(s[l])
                l += 1
            longestSubstringSize = max(longestSubstringSize, r - l + 1)
            visitedChars.add(char)

        return longestSubstringSize
