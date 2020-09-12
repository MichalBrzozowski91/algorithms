class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        '''We look for all Fibonacci triples a+b=c. Time complexity O(N^2)'''
        nums = A
        result = {} # List of results as a hashtable
        longest = 0 # Longest Fibonacci subsequence
        nums.sort() # We sort numbers
        if nums == []:
            return result
        for c in reversed(range(2,len(nums))):
            a, b = 0, c-1 # First pointer at the begining, second pointer at the end
            while a < b:
                s = nums[a]+nums[b] # Sum candidate
                if s == nums[c]: # Sum is equal to c
                    # We make a longer chain
                    if str([nums[b],nums[c]]) in result:
                        #print('Joining',nums[a],result[str([nums[b],nums[c]])])
                        result[str([nums[a],nums[b]])] = [nums[a]] + result[str([nums[b],nums[c]])]
                        longest = max(len(result[str([nums[a],nums[b]])]),longest)
                    else:
                        result[str([nums[a],nums[b]])] = [nums[a],nums[b],nums[c]]
                        longest = max(3,longest)
                    a += 1
                    b -= 1
                elif s > nums[c]: # Sum is too big
                    b -= 1
                elif s < nums[c]: #Sum is too small
                    a += 1
        return longest
