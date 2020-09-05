class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N = len(S)
        result = []
        deq = deque([])
        for i in range(N):
            if S[i] == 'I' and not deq:
                result.append(i)
            elif S[i] == 'I' and deq:
                deq.appendleft(i)
                result += list(deq)
                deq = deque([])
            elif S[i] == "D":
                deq.appendleft(i)
        # Last element
        if deq:
            deq.appendleft(N)
            result += list(deq)
        else:
            result.append(N)
        return result
                
