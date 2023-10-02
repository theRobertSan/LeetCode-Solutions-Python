from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        res = []

        def dfs(index: int, curSum: int, curValues: List[int]):
            if curSum == target:
                res.append(curValues.copy())
                return
            if index >= len(candidates) or curSum > target:
                return

            curValues.append(candidates[index])
            dfs(index, curSum + candidates[index], curValues)

            curValues.pop()
            dfs(index + 1, curSum, curValues)

        dfs(0, 0, [])
        return res
