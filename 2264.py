class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxDigit = -1
        count, curDigit = 0, -1

        for digit in num:
            if digit == curDigit:
                count += 1

                if count == 3:
                    maxDigit = max(maxDigit, int(digit))
                    count, curDigit = 0, -1
            else:
                curDigit, count = digit, 1

        return str(maxDigit) * 3 if maxDigit != -1 else ""
