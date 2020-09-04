class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Creating a hashtable with all letter latest appearances in O(N) time
        hashtable = {}
        for i in range(len(S)):
                hashtable[S[i]] = i
        # Creating partitions
        result = []
        counter = 0
        maxIndex = 0
        for i in range(len(S)):
            counter += 1
            maxIndex = max(maxIndex,hashtable[S[i]])
            if i == maxIndex: # We end the partition
                result.append(counter)
                counter = 0
                maxIndex = 0
        return result
