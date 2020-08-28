class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Two pointer solution
        nums.sort() # We sort numbers
        result = None # We store result here
        how_close = float('inf') # Closest distance to our target, we start at infinity
        for i in range(0,len(nums) - 2):
            j, k = i+1, len(nums) - 1 # Left and right pointers
            while k > j: # Right pointer must be bigger than left pointer
                #print(i,j,k)
                s = nums[i] + nums[j] + nums[k]
                
                if abs(target - s) < how_close: # If we are closer to our target we change the result and the smallest possible distance
                    how_close = abs(target - s)
                    result = s
                if s == target:
                    how_close = 0
                    result = s
                    return result # This is the closest one
                elif s > target: # It is too big, we make it smaller, making it bigger cannot be optimal (this is crucial to reduce complexity to O(N^2))
                    k -= 1
                elif s < target:
                    j += 1 # It is too small, we make it bigger, making it smaller cannot be optimal (this is crucial to reduce complexity to O(N^2))
        return result
