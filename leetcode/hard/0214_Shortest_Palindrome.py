class Solution:
    def shortestPalindrome(self, s: str) -> str:
        #print(len(s))
        if len(s) == 0:
            return ''
        for i in range(len(s),0,-1):
            if s[0:i] == s[i-1::-1]:
                return s[len(s)-1:i-1:-1] + s
