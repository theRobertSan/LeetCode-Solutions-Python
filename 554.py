from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        brickEdges = {}
        maxEdges = 0

        for brickRow in wall:
            curPos = 0
            for brick in brickRow[:-1]:
                curPos += brick
                brickEdges[curPos] = 1 + brickEdges.get(curPos, 0)
                maxEdges = max(maxEdges, brickEdges[curPos])

        return height - maxEdges
