class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        words.reverse()
        for word in words:
            if word:
                return len(word)
        return 0
