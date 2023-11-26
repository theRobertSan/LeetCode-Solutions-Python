from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seenPositions = set()

        def bt(row: int, col: int, index: int) -> bool:
            if (
                not (0 <= row < ROWS)
                or not (0 <= col < COLS)
                or (row, col) in seenPositions
                or board[row][col] != word[index]
            ):
                return False

            seenPositions.add((row, col))
            index += 1
            if index == len(word):
                return True

            for addRow, addCol in MOVES:
                if bt(row + addRow, col + addCol, index):
                    return True
            seenPositions.remove((row, col))

            return False

        for row in range(ROWS):
            for col in range(COLS):
                if bt(row, col, 0):
                    return True

        return False
