class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if not A: # A is empty
            return []
        Amax = max(A)
        index = A.index(Amax)
        # We do a pancake flip at index + 1
        #print(A)
        A = A[index::-1] + A[index+1:]
        #print('After pancake flip at',index,':',A)
        # We do a pancake flip at len(A) - 1
        A.reverse()
        #print('After pancake flip at ',len(A)-1,':',A)
        return [index+1,len(A)] + self.pancakeSort(A[:-1])
