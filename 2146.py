from collections import deque
from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        minPrice, maxPrice = pricing
        queue = deque([(start[0], start[1])])
        seenLoc = set()
        result = []

        def isNewValidLoc(row, col):
            return (
                (row, col) not in seenLoc and
                0 <= row < ROWS and
                0 <= col < COLS
            )

        while queue and k > 0:
            queueLen = len(queue)
            layerItems = []
            for _ in range(queueLen):
                row, col = queue.popleft()
                if not isNewValidLoc(row, col):
                    continue

                seenLoc.add((row, col))
                itemPrice = grid[row][col]

                if itemPrice > 0:
                    if itemPrice > 1 and minPrice <= itemPrice <= maxPrice:
                        layerItems.append((itemPrice, row, col))

                    queue.append((row - 1, col))
                    queue.append((row + 1, col))
                    queue.append((row, col - 1))
                    queue.append((row, col + 1))

            layerItems.sort()
            toRemove = min(k, len(layerItems))
            result.extend(map(
                lambda x: [x[1], x[2]],
                layerItems[:toRemove]
            ))
            k -= toRemove

        return result
