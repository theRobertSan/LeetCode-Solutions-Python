from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1, stack2 = [root1], [root2]

        def findNextLeaf(stack):
            while stack:
                curNode = stack.pop()
                if curNode.right is None and curNode.left is None:
                    return curNode

                if curNode.right:
                    stack.append(curNode.right)
                if curNode.left:
                    stack.append(curNode.left)

            return None

        while True:
            leaf1 = findNextLeaf(stack1)
            leaf2 = findNextLeaf(stack2)

            if leaf1 is None or leaf2 is None:
                return leaf1 is None and leaf2 is None

            if leaf1.val != leaf2.val:
                return False
