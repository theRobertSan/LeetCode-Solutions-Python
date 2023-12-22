class Solution:
    def maxScore(self, s: str) -> int:
        prefixZeroes, zeroes = [0], 0
        for num in s[:-1]:
            if num == "0":
                zeroes += 1
            prefixZeroes.append(zeroes)

        maxPoints = 0
        ones = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == "1":
                ones += 1
            maxPoints = max(maxPoints, ones + prefixZeroes[i])

        return maxPoints


print(Solution().maxScore("011101"))
