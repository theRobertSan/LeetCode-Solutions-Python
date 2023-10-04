from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenOranges = deque()
        fresh = time = 0

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rottenOranges.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while rottenOranges and fresh > 0:
            for _ in range(len(rottenOranges)):
                rottenOrange = rottenOranges.popleft()
                for rowMove, colMove in directions:
                    row, col = rottenOrange[0] + \
                        rowMove, rottenOrange[1] + colMove
                    if (0 <= row < rows and 0 <= col < cols
                            and grid[row][col] == 1):
                        grid[row][col] = 2
                        rottenOranges.append((row, col))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1
