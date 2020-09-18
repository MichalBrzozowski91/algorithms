class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Create a hashset:
        hashset = set()
        for letter in J:
            hashset.add(letter)
        counter = 0
        for letter in S:
            if letter in hashset:
                counter += 1
        return counter