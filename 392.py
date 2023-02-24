class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        index_s = 0
        for char_t in t:
            if char_t == s[index_s]:
                index_s += 1
                if index_s == len(s):
                    return True

        return False


print(Solution().isSubsequence("abcc", "ahbgdc"))
