# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        output = []

        if root is None:
            return output

        def dps(node: Node):
            output.append(node.val)

            if node.children:
                for child in node.children:
                    dps(child)

        dps(root)

        return output

    def preorder_iter(self, root: Node) -> List[int]:
        output = []

        if root is None:
            return output

        stack = deque()
        stack.append(root)

        while stack:
            popped_node = stack.pop()

            output.append(popped_node.val)

            if popped_node.children:
                for child in reversed(popped_node.children):
                    stack.append(child)

        return output
