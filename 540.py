from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while True:
            m = (l + r) // 2
            indexOfFirstOcc = m

            if m > 0 and nums[m] == nums[m - 1]:
                indexOfFirstOcc = m - 1
            elif m < len(nums) - 1 and nums[m] == nums[m + 1]:
                indexOfFirstOcc = m
            else:
                return nums[m]

            if indexOfFirstOcc % 2 == 0:
                l = indexOfFirstOcc + 2
            else:
                r = indexOfFirstOcc - 1

        return 0
