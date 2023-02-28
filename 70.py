class Solution:
    def climbStairs(self, n: int) -> int:
        curr, next = 2, 1

        for _ in range(n - 1):
            curr, next = curr + next, curr

        return next
