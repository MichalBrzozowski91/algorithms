class Solution:
    def helper(self, k, n, lower):
        '''Returns all k-element sets of numbers from [lower,9] which add up to n'''
        res = []
        if k > 9 or n > 45:
            return []
        digits = range(lower,10)
        if k == 1 and n in digits:
            return [[n]]
        if k == 1 and n not in digits:
            return []
        for i in digits:
            new = self.helper(k - 1, n - i, i + 1)
            for element in new:
                res.append([i] + element)
        return res
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.helper(k, n, 1)
