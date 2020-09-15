class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashsetelements = set()
        duplicates_count = 0
        for letter in s:
            if letter not in hashsetelements:
                hashsetelements.add(letter)
            else:
                duplicates_count += 1
                hashsetelements.remove(letter)
        if 2*duplicates_count == len(s):
            return 2*duplicates_count
        else:
            return 2*duplicates_count + 1