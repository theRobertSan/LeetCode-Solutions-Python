from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notDestSet, destSet = set(), set()

        for origin, dest in paths:
            if origin in destSet:
                destSet.remove(origin)

            notDestSet.add(origin)

            if dest not in notDestSet:
                destSet.add(dest)

        return list(destSet)[0]


print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
