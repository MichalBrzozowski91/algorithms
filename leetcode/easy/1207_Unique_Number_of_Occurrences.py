class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictmap = {}
        for i in arr:
            if i not in dictmap:
                dictmap[i] = 1
            else:
                dictmap[i] += 1
        vals = dictmap.values()
        return len(vals) == len(set(vals))