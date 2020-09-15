class Solution:
    def listOfNumbersWithStart(self,start,lenght, diff):
        result = []
        if lenght == 1:
            return [start]
        else:
            if start + diff <= 9:
                nextList = self.listOfNumbersWithStart(start + diff,lenght - 1, diff)
                for element in nextList:
                    result.append(str(start) + str(element))
            if start - diff >= 0 and diff != 0:
                nextList = self.listOfNumbersWithStart(start - diff,lenght - 1, diff)
                for element in nextList:
                    result.append(str(start) + str(element))
        return result

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        result = []
        for i in range(1,10): # All possible first digits
            result += self.listOfNumbersWithStart(i,N, K)
        # Translation to integers
        for i in range(len(result)):
            result[i] = int(result[i])
        return result   