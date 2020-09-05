class Solution:
    def ifSelfDividing(self,number):
        for digit in str(number):
            if digit == '0':
                return False
            elif number % int(digit) != 0:
                return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for number in range(left,right + 1):
            if self.ifSelfDividing(number):
                result.append(number)
        return result
