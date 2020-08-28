class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1 # Number of paths when we start from the 1st step
        b = 1 # Number of paths when we start from the 2nd step
        for i in range(0,n-1):
            a, b = a+b, a
        return a
