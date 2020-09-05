class Solution:
    def sortString(self, s: str) -> str:
        result = []
        x = [ord(letter) for letter in s]
        occ = {}
        for i in x:
            if i not in occ:
                occ[i] = 1
            else:
                occ[i] += 1
        letters = list(occ.keys())
        letters.sort()
        for i in range(len(s)):
            to_append = [letter for letter in letters if occ[letter] > i]
            if to_append == []:
                break
            result += to_append
            letters.reverse()
        word = [chr(x) for x in result]
        return ''.join(word)
        
