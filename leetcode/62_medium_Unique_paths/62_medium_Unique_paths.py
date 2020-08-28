class Solution:
    # Math solution
    def uniquePaths(self, m: int, n: int) -> int:
        import scipy.special
        return int(scipy.special.binom(m + n - 2, m - 1))
