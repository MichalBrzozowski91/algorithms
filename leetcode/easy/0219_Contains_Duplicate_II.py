class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Hash table solution
        numsdict = {} # Dictonary of the form value: index
        for i in range(len(nums)):
            if nums[i] in numsdict:
                if i - numsdict[nums[i]] <= k:
                    return True
            numsdict[nums[i]] = i
        return False
