from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        totalOp = 0
        for _, freq in freq.items():
            if freq == 1:
                return -1

            if freq % 3 == 0:
                totalOp += freq // 3
            else:
                totalOp += (freq // 3) + 1

        return totalOp
