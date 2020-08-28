class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach 4, using list comprehension:
        nums[:] = [x for x in nums if x!=val]
        return len(nums)
