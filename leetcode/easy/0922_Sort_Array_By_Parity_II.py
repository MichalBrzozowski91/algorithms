class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = [a for a in A if a % 2 == 0]
        even = [a for a in A if a % 2 == 1]
        result = []
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(odd.pop())
            else:
                result.append(even.pop())
        return result
