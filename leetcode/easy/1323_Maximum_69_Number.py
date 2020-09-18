class Solution:
    def maximum69Number (self, num: int) -> int:
        for i in range(len(str(num))):
            if str(num)[i] == '6':
                return int(str(num)[:i] + '9' + str(num)[i+1:])
        return num