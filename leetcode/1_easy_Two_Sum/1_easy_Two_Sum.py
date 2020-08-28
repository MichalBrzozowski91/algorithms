class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointer solution
        nums_copy = nums[:] # We make a copy by slicing
        nums.sort() # We sort numbers
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == target: # s is equal to a target:
                if nums[i] != nums[j]:
                    return[nums_copy.index(nums[i]),nums_copy.index(nums[j])]
                else:
                    return[nums_copy.index(nums[i]),(len(nums) - 1 - nums_copy[::-1].index(nums[j]))]
            elif s > target: # s is too big
                j -= 1
            elif s < target: # s is too small
                i += 1
        return None
