class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result_list = []
        for i in range(0,2*n):
            if i % 2 == 0:
                result_list.append(nums[int(i/2)]) # Odd index, we take x
            else:
                result_list.append(nums[n+int((i-1)/2)]) # Even index, we take y
        return result_list