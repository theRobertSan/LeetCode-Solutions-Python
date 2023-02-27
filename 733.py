from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        to_replace = image[sr][sc]

        if to_replace == color:
            return image

        def replace(sr: int, sc: int):
            # Out of bounds
            if (
                not 0 <= sr < len(image) or not 0 <= sc < len(image[0])
                or image[sr][sc] != to_replace
            ):
                return

            image[sr][sc] = color
            replace(sr - 1, sc)
            replace(sr, sc - 1)
            replace(sr + 1, sc)
            replace(sr, sc + 1)

        replace(sr, sc)

        return image
