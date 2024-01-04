class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for i in range(1, nodes + 1):
                total += numTree[i - 1] * numTree[nodes - i]
            numTree[nodes] = total
        return numTree[n]
