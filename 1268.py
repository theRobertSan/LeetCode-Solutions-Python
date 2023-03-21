from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, r = 0, len(products) - 1
        results = []

        for char_index, char in enumerate(searchWord):

            while l <= r and (len(products[l]) <= char_index or products[l][char_index] != char):
                l += 1

            while l <= r and (len(products[r]) <= char_index or products[r][char_index] != char):
                r -= 1

            elems = r - l + 1
            curr_result = []
            for i in range(min(elems, 3)):
                curr_result.append(products[l + i])

            results.append(curr_result)

        return results
