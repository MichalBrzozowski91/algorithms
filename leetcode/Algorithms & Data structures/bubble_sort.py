def bubble_sort(nums):
    flag = True
    no_of_swaps = 0
    while flag:
        flag = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                no_of_swaps += 1
                print('Swap',no_of_swaps,':',nums)
                flag = True # There was a swap, so we must run again
    return nums
