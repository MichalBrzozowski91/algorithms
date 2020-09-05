class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = len(s)
        result = [None] * l
        for i in range(l):
            result[indices[i]] = s[i]
        return ''.join(result)
