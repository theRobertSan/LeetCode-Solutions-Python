from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        maxRes = 0
        stack = []
        for i, num in enumerate(nums):
            startingIndex = i
            while stack and num < stack[-1][1]:
                otherI, otherNum = stack.pop()
                minProd = otherNum * (presum[i] - presum[otherI])
                maxRes = max(maxRes, minProd)
                startingIndex = otherI

            stack.append((startingIndex, num))

        while stack:
            otherI, otherNum = stack.pop()
            minProd = otherNum * (presum[-1] - presum[otherI])
            maxRes = max(maxRes, minProd)

        return maxRes % (10**9 + 7)
