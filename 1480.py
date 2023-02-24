from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_nums = [nums[0]]
        for num in nums[1:]:
            new_nums.append(new_nums[-1] + num)
        return new_nums


nums = [3, 1, 2, 10, 1]
print(Solution().runningSum(nums))
