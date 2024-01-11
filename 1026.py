from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(curNode: Optional[TreeNode], minVal: int, maxVal: int):
            if curNode is None:
                return 0

            minVal = min(minVal, curNode.val)
            maxVal = max(maxVal, curNode.val)

            return max(
                maxVal - minVal,
                dfs(curNode.left, minVal, maxVal),
                dfs(curNode.right, minVal, maxVal)
            )

        return dfs(root, root.val, root.val)
