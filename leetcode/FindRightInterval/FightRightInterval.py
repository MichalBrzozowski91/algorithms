# O(NlogN) time complexity, O(N) space complexity
class Solution:
    def findRightInterval(self, intervals):
        '''
        Input: list of intervals given as a list [start,point]
        Output: list of the closest intervals to the right , -1 if such an interval
        does not exist
        '''
        # Step 1: We create a dictionary mapping a starting point to the interval.
        # Recall that we assume that starting points are unique. 
        l = len(intervals)
        result = [0 for i in range(l)]
        dictstart = {intervals[i][0]: i for i in range(l)}
        # We create a list of all starting points
        startlist = [interval[0] for interval in intervals]
        
        # Step 2: We sort all the starting points in the ascending order in-place
        startlist.sort()
        # Step 3: We sort all intervals based on the endpoint of the interval
        intervals.sort(key = lambda x: x[1])
        # Step 4: Loop over a sorted list of intervals
        # We create a pointer to one-pass sorted list of all starting points startlist
        pointer = 0
        for i in range(l):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]
            while pointer < l:
                if startlist[pointer] >= end:
                    endindex = dictstart[start]
                    startindex = dictstart[startlist[pointer]]
                    result[endindex] = startindex
                    break
                pointer += 1
            # We finished passing a starting list, hence the function return -1
            if pointer == l:
                endindex = dictstart[start]
                result[endindex] = -1
        return result
