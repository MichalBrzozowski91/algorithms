class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = {}
        for i in range(len(arr2)):
            index[arr2[i]] = i
        inarr2 = [x for x in arr1 if x in index]
        rest = [x for x in arr1 if x not in index]
        inarr2.sort(key = lambda x: index[x])
        rest.sort()
        return inarr2 + rest
