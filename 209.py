import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = curSum = 0
        minLen = math.inf

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minLen = min(minLen, r - l + 1)
                if minLen == 1:
                    return minLen
                curSum -= nums[l]
                l += 1

        return minLen if minLen != math.inf else 0
