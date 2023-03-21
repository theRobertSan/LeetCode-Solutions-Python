class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        skip_s = skip_t = 0
        pointer_s, pointer_t = len(s) - 1, len(t) - 1

        while pointer_s >= 0 or pointer_t >= 0:

            while pointer_s >= 0:
                if s[pointer_s] == "#":
                    skip_s += 1
                    pointer_s -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    pointer_s -= 1
                else:
                    break

            while pointer_t >= 0:
                if t[pointer_t] == "#":
                    skip_t += 1
                    pointer_t -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    pointer_t -= 1
                else:
                    break

            if (pointer_s >= 0 and pointer_t >= 0 and
                    s[pointer_s] != t[pointer_t]):
                return False

            if (pointer_s >= 0) != (pointer_t >= 0):
                return False

            pointer_s -= 1
            pointer_t -= 1

        return True
