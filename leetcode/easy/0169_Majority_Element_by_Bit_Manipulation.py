# Bit manipulation solution
class Solution:
    def majorityElement(self, nums):
        res = ''
        for i in range(32):
            count_0 = 0
            count_1 = 0
            for num in nums:
                binary = bin(abs(num))[2:]
                try:
                    digit = binary[-i-1]
                except IndexError:
                    digit = '0'
                count_0 += 1 - int(digit)
                count_1 += int(digit)
            if count_1 > count_0:
                res += '1'
            else:
                res += '0'
        result = int(res[::-1],2)
        # Checking a count
        plus = sum(1 for num in nums if num == result)
        minus = sum(1 for num in nums if num == - result)
        if plus > minus:
            return result
        else:
            return -result
