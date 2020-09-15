from math import log
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return log(num,4) == int(log(num,4))