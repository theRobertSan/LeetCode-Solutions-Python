from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = {0: 1}
        res = curCount = 0

        for num in nums:
            curCount += num
            neededPrefix = curCount - k

            res += prefixCount.get(neededPrefix, 0)
            prefixCount[curCount] = 1 + prefixCount.get(curCount, 0)

        return res
