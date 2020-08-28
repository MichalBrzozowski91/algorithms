class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] # List of results
        nums.sort() # We sort numbers
        if nums == []:
            return result
        if nums[0] > 0:
            return result
        for l1 in range(0,len(nums)-3): #First left pointer
            if l1 > 0 and nums[l1] == nums[l1-1]: # We want to eliminate duplicates 
                continue
            for l2 in range(l1+1,len(nums)-2): # Second left pointer
                if l2 > l1+1 and nums[l2] == nums[l2-1]: # We want to eliminate duplicates
                    continue
                r1, r2 = l2+1, len(nums)-1 # First right pointer at the begining, second right pointer at the end
                while r1 < r2: # Right pointers must be bigger than left pointers
                    #print('Pointers:',l1,l2,r1,r2)
                    s = nums[l1] + nums[l2] + nums[r1] + nums[r2] # Sum candidate
                    if s == target: # Sum is equal to the target
                        if result == [] or result[-1] != [nums[l1],nums[l2],nums[r1],nums[r2]]:
                            result.append([nums[l1],nums[l2],nums[r1],nums[r2]])
                        r1 += 1
                        r2 -= 1
                    elif s > target: # Sum is too big
                        r2 -= 1
                    elif s < target: #Sum is too small
                        r1 += 1
        return result
