from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        nums = []

        def isValidIpNum(startIndex: int, endIndex: int):
            ipNum = s[startIndex: endIndex]
            if ipNum == "0":
                return True
            return int(ipNum) <= 255 and s[startIndex] != "0"

        def backtracking(dotPos: int):
            if len(s) - dotPos > 12 - (len(nums) * 3):
                return

            if len(nums) == 3 and isValidIpNum(dotPos, len(s)):
                nums.append(s[dotPos:len(s)])
                result.append(".".join(nums))
                nums.pop()
                return

            nextDotPos = dotPos + 1
            while isValidIpNum(dotPos, nextDotPos) and nextDotPos < len(s):
                nums.append(s[dotPos:nextDotPos])
                backtracking(nextDotPos)
                nums.pop()
                nextDotPos += 1

        backtracking(0)
        return result
