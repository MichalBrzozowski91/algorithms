class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: # Empty list
            return 0
        intervals = sorted(intervals,key = lambda x: x[0]) # We sort the intervals by the first endpoint
        counter = 0
        result = 0
        endpoint = float(inf)
        for element in intervals:
            if endpoint <= element[0]: # We decide to eliminate counter - 1 intervals considered before (they all overlap with each other and the current one)
                result += counter - 1
                counter = 0
                endpoint = float(inf)
            counter += 1
            endpoint = min(endpoint,element[1])
        result += counter - 1
        return result
