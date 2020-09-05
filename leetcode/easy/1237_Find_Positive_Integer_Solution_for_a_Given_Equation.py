"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        i = 1
        while True:
            if customfunction.f(i,1) == z:
                result.append([i,1])
                i_max = i
                break
            elif customfunction.f(i,1) < z:
                i += 1
            elif customfunction.f(i,1) > z:
                i_max = i
                break
        i = 1
        for i in range(1,i_max):
            j = 2
            while True:
                if customfunction.f(i,j) == z:
                    result.append([i,j])
                    break
                elif customfunction.f(i,j) < z:
                    j += 1
                elif customfunction.f(i,j) > z:
                    break
        return result
