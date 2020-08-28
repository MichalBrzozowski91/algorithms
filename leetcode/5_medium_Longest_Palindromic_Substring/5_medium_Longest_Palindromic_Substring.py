class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(len(s))
        longest_palindrome = ''
        d = []
        # Search O(n)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                d.append([i,i+1])
            if i < len(s)-2 and s[i] == s[i+2]:
                d.append([i,i+2])
        # Palindrome search O(n^2)
        for i in range(len(d)):
            while d[i][0]>0 and d[i][1]+1<len(s) and s[d[i][0]-1] == s[d[i][1]+1]:
                # Enlarging a palindrome:
                d[i][0] = d[i][0]-1
                d[i][1] = d[i][1]+1
            if d[i][1] - d[i][0] + 1 > len(longest_palindrome):
                longest_palindrome = s[d[i][0]:d[i][1]+1]
        # No palindromes
        if longest_palindrome == '' and len(s) > 0:
            longest_palindrome = s[0]
        return longest_palindrome
