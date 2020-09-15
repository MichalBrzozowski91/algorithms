class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        i = 0
        for letter in s[::-1]:
            number = ord(letter) - 64
            #print(letter,ord(letter),number)
            result += number*(26**i)
            i += 1
        return result