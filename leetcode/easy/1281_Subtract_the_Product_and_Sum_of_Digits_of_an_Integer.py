class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        SumOfDigits = 0
        ProductOfDigits = 1
        for letter in str(n):
            SumOfDigits += int(letter)
            ProductOfDigits *= int(letter)
        return  ProductOfDigits - SumOfDigits
        