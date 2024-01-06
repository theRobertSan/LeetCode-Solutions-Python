from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i: int):
            if i == len(jobs):
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i+1)

            l, r = i + 1, len(jobs) - 1

            while l <= r:
                m = (l + r) // 2
                if jobs[i][1] <= jobs[m][0]:
                    r = m - 1
                else:
                    l = m + 1

            res = max(res, jobs[i][2] + dfs(l))
            cache[i] = res
            return res

        return dfs(0)
