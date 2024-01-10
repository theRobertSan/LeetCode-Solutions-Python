# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        nodeNeigh = defaultdict(list)
        startNode = None

        def buildNodeNeigh(prevNode, curNode):
            nonlocal startNode

            if curNode.val == start:
                startNode = curNode

            if prevNode:
                nodeNeigh[curNode.val].append(prevNode)
            if curNode.left:
                nodeNeigh[curNode.val].append(curNode.left)
                buildNodeNeigh(curNode, curNode.left)
            if curNode.right:
                nodeNeigh[curNode.val].append(curNode.right)
                buildNodeNeigh(curNode, curNode.right)

        buildNodeNeigh(None, root)

        seenNodes = set()
        queue = deque([startNode])
        minutes = -1

        while queue:
            for _ in len(queue):
                curNode = queue.popleft()
                seenNodes.add(curNode)

                for neighNode in nodeNeigh[curNode]:
                    if neighNode not in seenNodes:
                        queue.append(neighNode)

            minutes += 1

        return minutes
