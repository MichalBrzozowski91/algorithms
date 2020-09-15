class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer solution
        nums = numbers
        nums.sort() # We sort numbers
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == target: # s is equal to a target:
                return True
            elif s > target: # s is too big
                j -= 1
            elif s < target: # s is too small
                i += 1
        return False