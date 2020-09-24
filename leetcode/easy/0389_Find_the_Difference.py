class Solution:
    def findTheDifference(self, s, t):
        hashmap = {}
        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        for letter in t:
            if letter in hashmap and hashmap[letter] != 0:
                hashmap[letter] -= 1
            else:
                return letter
