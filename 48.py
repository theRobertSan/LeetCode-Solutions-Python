from pprint import pprint
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1

        for j in range(n):
            for i in range(j, n-j):
                matrix[j][i], matrix[i][n-j], matrix[n-j][n-i], matrix[n-i][j] = (
                    matrix[n-i][j],
                    matrix[j][i],
                    matrix[i][n-j],
                    matrix[n-j][n-i]
                )
