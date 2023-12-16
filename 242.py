from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharFreq = defaultdict(int)

        for sChar in s:
            sCharFreq[sChar] += 1

        for tChar in t:
            if tChar not in sCharFreq:
                return False
            sCharFreq[tChar] -= 1

            if sCharFreq[tChar] == 0:
                sCharFreq.pop(tChar)

        return len(sCharFreq) == 0
