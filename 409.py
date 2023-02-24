class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set()

        for char in s:
            if char in letters:
                letters.remove(char)
            else:
                letters.add(char)

        return len(s) if len(letters) == 0 else len(s) - len(letters) + 1


print(Solution().longestPalindrome("a"))
