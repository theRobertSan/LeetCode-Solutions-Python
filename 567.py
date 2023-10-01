class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        print(s1Count)
        print(s2Count)

        for count1, count2 in zip(s1Count, s2Count):
            if count1 == count2:
                matches += 1
        print(matches)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            rightIndex = ord(s2[r]) - ord("a")
            s2Count[rightIndex] += 1
            if s2Count[rightIndex] == s1Count[rightIndex]:
                matches += 1
            elif s2Count[rightIndex] == s1Count[rightIndex] + 1:
                matches -= 1

            leftIndex = ord(s2[l]) - ord("a")
            s2Count[leftIndex] -= 1
            if s2Count[leftIndex] == s1Count[leftIndex]:
                matches += 1
            elif s2Count[leftIndex] == s1Count[leftIndex] - 1:
                matches -= 1

            l += 1

        return matches == 26
