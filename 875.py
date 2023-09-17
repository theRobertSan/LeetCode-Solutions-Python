import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        bestK = r

        while l <= r:
            m = (r + l) // 2

            hoursSpent = 0
            for pile in piles:
                hoursSpent += math.ceil(pile / m)

            if hoursSpent > h:
                l = m + 1
            else:
                r = m - 1
                bestK = min(bestK, m)

        return bestK
