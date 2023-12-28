from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        deletions = 0

        prevEnd = intervals[0][1]
        for curStart, curEnd in intervals[1:]:
            if curStart < prevEnd:
                deletions += 1
                prevEnd = min(prevEnd, curEnd)
            else:
                prevEnd = curEnd

        return deletions
