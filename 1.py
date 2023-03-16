from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for index, num in enumerate(nums):
            if num in differences:
                return [differences[num], index]

            differences[target - num] = index

        return None
