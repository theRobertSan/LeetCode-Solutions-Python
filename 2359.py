from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        curNode1, curNode2 = node1, node2
        ended1 = ended2 = False
        visited1, visited2 = set(), set()

        while True:
            if ended1 and ended2:
                return -1
            if curNode1 == curNode2:
                return curNode1

            c1Found = curNode1 in visited2
            c2Found = curNode2 in visited1

            if c1Found and c2Found:
                return min(curNode1, curNode2)
            if c1Found:
                return curNode1
            if c2Found:
                return curNode2

            if not ended1:
                visited1.add(curNode1)
                curNode1 = edges[curNode1]
            if not ended2:
                visited2.add(curNode2)
                curNode2 = edges[curNode2]

            if curNode1 == -1 or curNode1 in visited1:
                ended1 = True
            if curNode2 == -1 or curNode2 in visited2:
                ended2 = True
