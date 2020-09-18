class Solution: # Two pointer in-place solution
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = len(A)
        j = 0
        for i in range(l):
            if A[j] % 2 == 0: # A[j] is even
                j += 1
            else: # A[j] is odd
                A = A[:j] + A[j+1:] + [A[j]]
        return A