from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = maxWallLeft = maxWallRight = 0

        while l < r:
            if height[l] <= height[r]:
                maxWallLeft = max(maxWallLeft, height[l])
                water += maxWallLeft - height[l]
                l += 1
            else:
                maxWallRight = max(maxWallRight, height[r])
                water += maxWallRight - height[r]
                r -= 1

        return water
