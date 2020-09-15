class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # k < 0:
        if k < 0:
            return 0
        # Creating a hash table O(n)
        pairs = []
        count_plus = 0
        hashtable_plus = {}
        for i in range(len(nums)):
            hashtable_plus[str(nums[i]+k)] = i
        print(hashtable_plus)
        # Hashtable search
        # k != 0
        if k == 0:
            result = 0
            for i in list(range(len(nums))):
                if str(nums[i]) in hashtable_plus and hashtable_plus[str(nums[i])] != i:
                    print(nums[i],hashtable_plus[str(nums[i])],i)
                    del hashtable_plus[str(nums[i])]
                    result += 1
            return result
        for n in nums:
            if str(n) in hashtable_plus:
                pairs.append((n,n-k))

        return len(set(pairs))
            