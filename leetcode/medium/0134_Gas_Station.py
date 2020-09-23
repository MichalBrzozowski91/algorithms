class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total = [gas[i] - cost[i] for i in range(n)]
        left_sum = [0 for _ in range(n)]
        left_min = [0 for _ in range(n)]
        right_min = [0 for _ in range(n)]
        current_sum = 0
        current_min = float('inf')
        for i in range(n):
            current_sum += total[i]
            left_sum[i] = current_sum
            current_min = min(current_min,current_sum)
            left_min[i] = current_min
        current_min = float('inf')
        for i in reversed(range(n)):
            current_min = min(current_min,left_sum[i])
            right_min[i] = current_min

        # Station 0
        if right_min[0] >= 0:
            return 0
        # Stations from 1 to n-1
        for i in range(1,n):
            if min(right_min[i],left_min[i-1] + left_sum[n-1]) - left_sum[i - 1] >= 0:
                return i
        return - 1
