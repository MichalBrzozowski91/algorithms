class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Creating hash table
        hash_table = {}
        number_of_pairs = 0
        for n in nums:
            if str(n) not in hash_table:
                hash_table[str(n)] = 1
            else:
                number_of_pairs += hash_table[str(n)]
                hash_table[str(n)] += 1
        return number_of_pairs