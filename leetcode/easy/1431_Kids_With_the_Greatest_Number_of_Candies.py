class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        # A kid can have the greatest number of candies if he already has max_candy - extraCandies
        result_list = [i >= max_candy - extraCandies for i in candies]
        return result_list