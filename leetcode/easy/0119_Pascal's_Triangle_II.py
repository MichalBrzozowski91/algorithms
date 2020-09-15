class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if rowIndex == 0:
            return result
        for i in range(1,rowIndex + 1):
            for j in range(i-1):
                result[j] = result[j] + result[j+1]
            result = [1] + result[:len(result)-1] + [1]
            #print(result)
        return result