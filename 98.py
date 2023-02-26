from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidSubTree(root, -math.inf, math.inf)

    def isValidSubTree(self, curr: Optional[TreeNode], min: int, max: int) -> bool:
        if curr is None:
            return True

        if not (min < curr.val < max):
            return False

        return (
            self.isValidSubTree(curr.left, min, curr.val)
            and self.isValidSubTree(curr.right, curr.val, max)
        )
