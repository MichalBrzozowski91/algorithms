class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0] # Start point of the new interval
        end = newInterval[1] # End point of the new interval
        intervalsLeft = [] # Here we will store a list of all intervals on the left of a new interval
        intervalsRight = [] # Here we will store a list of all intervals on the left of a new interval
        left = start # Here we will store a start point of a bigger interval
        right = end # Here we will store an end point of a bigger interval
        for i in range(len(intervals)):
            p = intervals[i][0]
            q = intervals[i][1]
            if start > q: # Interval [p,q] is on the left of a new interval
                intervalsLeft.append(intervals[i])
            elif p > end: # Interval [p,q] is on the right of a new interval
                intervalsRight.append(intervals[i])
            else: # Interval [p,q] will be covered by a bigger interval, hence we update values of left and right 
                left = min(left,p)
                right = max(right,q)
        return intervalsLeft + [[left,right]] + intervalsRight
