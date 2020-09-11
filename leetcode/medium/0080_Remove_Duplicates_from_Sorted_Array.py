class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 1
        for j in range(2,len(nums)):
            #print(i,j,nums)
            if nums[i] != nums[j] or nums[i-1] != nums[j]:
                i+=1
                nums[i] = nums[j]
                
        return i + 1
