class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        s = sum(nums)
        current_sum = None
        result = []
        while True:
            number = nums.pop()
            result.append(number)
            if current_sum == None:
                current_sum = number
            else:
                current_sum += number
            if current_sum > s/2:
                return result
            
