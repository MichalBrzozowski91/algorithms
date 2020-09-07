class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        if k == 0:
            return nums
        print(k)
        copy = nums.copy()
        for i in range(N):
            nums[i] = copy[(i-k)%N]
