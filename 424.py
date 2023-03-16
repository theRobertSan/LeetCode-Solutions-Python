class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        max_f = 0
        max_length = 0

        for r in range(len(s)):
            # Get letter at r position
            letter = s[r]
            # Update frequency of letter
            frequency[letter] = frequency.get(letter, 0) + 1
            max_f = max(max_f, frequency[letter])

            while r - l + 1 - max_f > k:
                frequency[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
