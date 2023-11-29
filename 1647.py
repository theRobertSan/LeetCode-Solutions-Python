class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        seenCounts = set()
        deletions = 0
        for count in freq.values():
            while count in seenCounts and count != 0:
                count -= 1
                deletions += 1

            if count != 0:
                seenCounts.add(count)

        return deletions
