class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for j in range(1,l):
            #print(j,l,s[j])
            if s[j] == s[0] and l % (j) == 0:
                #print(j)
                k = int(l / (j))
                if s[:j]*k == s:
                    return True
        return False
