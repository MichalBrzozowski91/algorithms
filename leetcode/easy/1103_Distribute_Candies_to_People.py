class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0 # current person index
        s = 1 # current candy amount to give
        while True:
            if s <= candies: # We can give this quantity of candies
                result[i] += s
                candies -= s
                s += 1
                i = (i + 1) % num_people # Cycling
            else:
                result[i] += candies # We give all the candies
                return result
                