class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        # Two pointer solution O(N) time, O(1) space
        i = 0
        j = 0
        n = len(nums)
        product = nums[0]
        result = 0
        while True:
            if product >= k and i == j: # nums[i] is larger than k, we skip this j 
                j += 1
                if j < n:
                    product *= nums[j]
                    continue
                else:
                    break
            elif product >= k: # We move i to the right
                product /= nums[i]
                i += 1
                continue
            else: # We found a subsequence
                result += (j - i) + 1
                j += 1
                if j < n:
                    product *= nums[j]
                    continue
                else:
                    break
        return result
