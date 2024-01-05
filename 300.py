from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        finalMaxLength = 0
        bestLengths = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            curNum = nums[i]
            for j in range(i + 1, len(nums)):
                if curNum < nums[j]:
                    bestLengths[i] = max(bestLengths[i], 1 + bestLengths[j])

            finalMaxLength = max(finalMaxLength, bestLengths[i])

        return finalMaxLength
