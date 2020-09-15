class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        B = A.copy()
        for firstDigitLimit in [2,1]:
            A = B.copy()
            result = ''
            temp = [a for a in A if a in range(firstDigitLimit + 1)]
            if not temp:
                return ''
            dig = max(temp)
            result += str(dig)
            A.remove(dig)
            # Second digit
            if dig == 2:
                temp = [a for a in A if a in [0,1,2,3]]
            else:
                temp = A
            if not temp:
                continue
            dig = max(temp)
            result += str(dig)
            A.remove(dig)
            # Third digit
            temp = [a for a in A if a in [0,1,2,3,4,5]]
            if not temp:
                continue
            dig = max(temp)
            result += ':' + str(dig)
            A.remove(dig)
            # Fourth digit
            dig = A[0]
            result += str(dig)
            return result
        return ''