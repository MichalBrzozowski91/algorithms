class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        '''Brute force O(N^4) solution'''
        N = len(A)
        # List of all 1 positions in A
        list1 = []
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1:
                    list1.append([i,j])
        # Set of all 1 positions in B
        set1 = set()
        for i in range(N):
            for j in range(N):
                if B[i][j] == 1:
                    set1.add((i,j))
        res = 0
        for l in range(- N + 1, N - 1 + 1): # Left translation vector
            for u in range(- N + 1, N - 1 + 1): # Up translation vector
               counter = 0
               for i,j in list1:
                   if (i+l,u+j) in set1:
                       counter += 1
               res = max(res,counter)  
        return res
