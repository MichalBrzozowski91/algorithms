class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Count bulls and put numbers in a dictionary
        secret_dict = {i:0 for i in range(10)}
        guess_dict = {i:0 for i in range(10)}
        bull_counter = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull_counter += 1
            else:
                secret_dict[int(secret[i])] += 1
                guess_dict[int(guess[i])] += 1
        # Count cows
        cow_counter = sum([min(secret_dict[i],guess_dict[i]) for i in range(10)])
        return str(bull_counter) + 'A' + str(cow_counter) + 'B'
