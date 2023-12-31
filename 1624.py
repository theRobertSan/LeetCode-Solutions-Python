class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstOcc = {}
        maxSize = -1

        for i, char in enumerate(s):
            if char not in firstOcc:
                firstOcc[char] = i
            else:
                maxSize = max(maxSize, i - firstOcc[char] - 1)

        return maxSize
