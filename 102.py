# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        if root is None:
            return output

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                popped_node = queue.popleft()
                level.append(popped_node.val)
                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                    queue.append(popped_node.right)

            output.append(level)

        return output
