class Solution():
    def getHint(self, secret: str, guess: str) -> str:
        secret_unmatched, guess_unmatched = {}, {}
        bulls = cows = 0

        for secret_char, guess_char in zip(secret, guess):
            # Matches perfectly
            if secret_char == guess_char:
                bulls += 1
            else:
                # Verify that secret char matches with previously seen char in guess
                cows = self.verify_match(
                    cows, secret_char, guess_unmatched, secret_unmatched)

                # Verify that guess char matches with previously seen char in secret
                cows = self.verify_match(
                    cows, guess_char, secret_unmatched, guess_unmatched)

        return f"{bulls}A{cows}B"

    def verify_match(self, cows: int, char_val: str, unmatched_verify: dict, unmatched_add: dict):
        if char_val in unmatched_verify:
            unmatched_verify[char_val] -= 1
            if unmatched_verify[char_val] == 0:
                del unmatched_verify[char_val]
            return cows + 1

        unmatched_add[char_val] = 1 + unmatched_add.get(char_val, 0)
        return cows
