class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()
        partitions = 1

        for char in s:
            if char in visited:
                visited = set()
                partitions += 1

            visited.add(char)

        return partitions
