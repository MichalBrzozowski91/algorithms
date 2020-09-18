class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = high - low + 1
        if count % 2 == 0:
            return int(count / 2)
        elif low % 2 != 0:
            return int((count+1)/2)
        else:
            return int((count-1)/2)
            