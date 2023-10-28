from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        p = 0

        while p <= r:
            if nums[p] == 0:
                nums[l], nums[p] = nums[p], nums[l]
                l += 1
                p += 1
            elif nums[p] == 2:
                nums[r], nums[p] = nums[p], nums[r]
                r -= 1
            else:
                p += 1
