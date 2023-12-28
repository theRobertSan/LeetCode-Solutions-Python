from ast import List
from collections import defaultdict


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        maxEarnings = [0] * (n+1)
        ridesMap = defaultdict(list)

        for start, end, tip in rides:
            ridesMap[end].append((start, tip))

        for end in range(2, n+1):
            bestSoFar = maxEarnings[end-1]

            for start, tip in ridesMap[end]:
                bestSoFar = max(
                    bestSoFar,
                    end - start + tip + maxEarnings[start]
                )

            maxEarnings[end] = bestSoFar

        return maxEarnings[-1]
