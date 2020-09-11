class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries == []:
            return 0
        poison_time = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration < timeSeries[i+1]:
                poison_time += duration
            else:
                poison_time += timeSeries[i+1] - timeSeries[i]
        poison_time += duration
        return poison_time
