from collections import deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = 1 + freq.get(task, 0)

        maxHeap = [-value for value in freq.values()]
        heapq.heapify(maxHeap)

        waiting = deque()
        time = 0

        while maxHeap or waiting:
            if maxHeap:
                topFreq = heapq.heappop(maxHeap) + 1
                if topFreq < 0:
                    waiting.append((topFreq, time + n))

            if waiting and waiting[0][1] == time:
                heapq.heappush(maxHeap, waiting.popleft()[0])

            time += 1

        return time
