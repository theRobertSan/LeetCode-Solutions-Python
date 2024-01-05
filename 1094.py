import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))

        dropOff = []
        curPass = 0
        for numPass, fr, to in trips:
            while dropOff and fr >= dropOff[0][0]:
                curPass -= heapq.heappop(dropOff)[1]

            curPass += numPass
            if curPass > capacity:
                return False

            heapq.heappush(dropOff, (to, numPass))

        return True
