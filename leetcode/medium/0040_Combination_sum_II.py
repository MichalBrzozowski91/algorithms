class Solution:
    def helper(self, candidates,target, s):
        '''We skip s first candidates'''
        res = []
        previous = None
        for i in range(s,len(candidates)):
            if candidates[i] == previous: # Skip duplicates
                continue
            previous = candidates[i]
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                res.append([candidates[i]])
                break
            new = self.helper(candidates, target - candidates[i], i + 1)
            for element in new:
               res.append([candidates[i]] + element)
        return res
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(candidates, target, 0)
