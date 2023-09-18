# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGoodNode(maxValueInPath, node):
            if node is None:
                return 0

            newMaxValue = max(node.val, maxValueInPath)

            return (
                (1 if (node.val >= maxValueInPath) else 0)
                + isGoodNode(newMaxValue, node.left)
                + isGoodNode(newMaxValue, node.right)
            )

        return isGoodNode(root.val, root)
