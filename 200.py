from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = [[False] * COLS for _ in range(ROWS)]

        def explore(row: int, col: int):
            if (
                not 0 <= row < ROWS or not 0 <= col < COLS
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "0"
            explore(row + 1, col)
            explore(row, col + 1)
            explore(row - 1, col)
            explore(row, col - 1)

        islands = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    explore(row, col)
                    islands += 1
        return islands
