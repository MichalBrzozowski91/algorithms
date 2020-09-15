class Solution:
    def isPalindrome(self, s: str) -> bool:
        return re.sub(r'[^a-zA-Z0-9]+','',s).lower() == re.sub(r'[^a-zA-Z0-9]+','',s).lower()[::-1]