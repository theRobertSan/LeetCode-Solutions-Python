from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mSum = sum(rolls)
        mPlusN = len(rolls) + n
        leftNSum = mean * mPlusN - mSum

        if leftNSum < n or leftNSum > 6 * n:
            return []

        result = [1] * n
        leftNSum -= n

        i = 0
        while leftNSum != 0:
            if leftNSum >= 5:
                leftNSum -= 5
                result[i] = 6
            else:
                result[i] += leftNSum
                leftNSum = 0
            i += 1

        return result
