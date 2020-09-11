class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # O(N) solution - without sorting
        N = len(citations)
        counting_list = [0]*(N+1)
        for i in range(N):
            counting_list[min(citations[i],N)] += 1
        
        #print(counting_list)
        count = 0
        for i in reversed(range(N+1)):
            count += counting_list[i]
            if count >= i:
                return i
        return 0
                
