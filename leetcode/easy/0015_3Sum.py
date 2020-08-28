class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] # List of results
        nums.sort() # We sort numbers
        if nums == []:
            return result
        if nums[0] > 0:
            return result
        for i in range(0,len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue # To avoid duplicates we dont repeat checking this number
            j, k = i+1, len(nums)-1 # First pointer at the begining, second pointer at the end
            while k > j:
                s = nums[i] + nums[j] + nums[k] # Sum candidate
                if s == 0: # Sum is equal to 0
                    if result == [] or result[-1] != [nums[i],nums[j],nums[k]]:
                        result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    
                elif s > 0: # Sum is too big
                    k -= 1
                elif s < 0: #Sum is too small
                    j += 1
        return result
