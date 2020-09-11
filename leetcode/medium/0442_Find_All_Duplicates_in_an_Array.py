class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(n) time no extra space solution
        result = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                result.append(abs(nums[i]))
            nums[abs(nums[i])-1] *= -1 # We make it negative
            #print(i,nums,result)
        return result
