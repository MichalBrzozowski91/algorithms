class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        seen = set()
        if len(words) != len(pattern):
            return False
        dictionary = {}
        for i,letter in enumerate(pattern):
            if letter in dictionary:
                if dictionary[letter] != words[i]:
                    return False
            elif words[i] in seen:
                return False
            else:
                dictionary[letter] = words[i]
                seen.add(words[i])
        return True
