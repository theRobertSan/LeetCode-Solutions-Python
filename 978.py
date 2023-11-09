from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxSize, currSize = 1, 0
        needSmaller = None

        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                maxSize, currSize = max(maxSize, currSize), 0
                needSmaller = None
            elif needSmaller is None:
                currSize = 2
                needSmaller = arr[i] > arr[i + 1]
            elif (arr[i] < arr[i + 1] and needSmaller) or (
                arr[i] > arr[i + 1] and not needSmaller
            ):
                currSize += 1
                needSmaller = not needSmaller
            else:
                maxSize, currSize = max(maxSize, currSize), 2
                needSmaller = arr[i] > arr[i + 1]

        maxSize = max(maxSize, currSize)

        return maxSize
