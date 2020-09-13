# O(N) time O(1) space solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0] # Start point of the new interval
        end = newInterval[1] # End point of the new interval
        left = start # Here we will store a start point of a bigger interval
        right = end # Here we will store an end point of a bigger interval
        i = 0
        while i < len(intervals):
            p = intervals[i][0]
            q = intervals[i][1]
            if start > q: # Interval [p,q] is on the left of a new interval
                i += 1
                continue
            elif p > end: # Interval [p,q] is on the right of a new interval, hence we insert
                intervals.insert(i,[left,right])
                return intervals
            else: # Interval [p,q] will be covered by a bigger interval, henve we delete it
                left = min(left,p)
                right = max(right,q)
                del intervals[i]
        intervals.append([left,right])
        return intervals
