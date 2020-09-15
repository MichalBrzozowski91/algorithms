class Solution:
    def bitinvert(self,x): #bitwise invert except the first position
        result = '1'
        for i in range(1,len(x)):
            result += str(1-int(x[i]))
        return result
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == '1':
            return [1]
        bin_rep = bin(label)[2:]
        lenght = len(bin_rep)
        result = [label]
        while bin_rep != '1':
            x = bin_rep[:-1] # We eliminate last digit
            x = self.bitinvert(x)
            result.append(int(x,2))
            bin_rep = x
            #print(result)
        return reversed(result)