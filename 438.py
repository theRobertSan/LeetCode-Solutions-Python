from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count, s_count = {}, {}

        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)

        result = [0] if s_count == p_count else []
        l = 0

        for r in range(len(p), len(s)):
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                s_count.pop(s[l])
            s_count[s[r]] = 1 + s_count.get(s[r], 0)

            l += 1

            if s_count == p_count:
                result.append(l)

        return result
