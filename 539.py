from math import inf
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        minDiff = inf

        for i in range(len(timePoints) - 1):
            timePoint1 = timePoints[i]
            timePoint2 = timePoints[i + 1]

            hoursDiff = int(timePoint2[:2]) - int(timePoint1[:2])
            minutesDiff = int(timePoint2[3:]) - int(timePoint1[3:])

            curDiff = hoursDiff * 60 + minutesDiff
            minDiff = min(minDiff, curDiff)

        hoursDiff = 24 - int(timePoints[-1][:2]) + int(timePoints[0][:2])
        minutesDiff = int(timePoints[0][3:]) - int(timePoints[-1][3:])
        curDiff = hoursDiff * 60 + minutesDiff
        minDiff = min(minDiff, curDiff)

        return minDiff
