class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        currentSum = 0
        for n in nums:
            currentSum += n
            runningSum.append(currentSum)
        return runningSum