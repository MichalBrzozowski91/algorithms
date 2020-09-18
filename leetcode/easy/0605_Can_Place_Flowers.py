class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        number_of_new_flowers = 0
        if n == 0:
            return True
        if flowerbed == [1]:
            return False
        if flowerbed == [0] and n==1:
            return True
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[1] == 0:
                    flowerbed[0] = 1
                    number_of_new_flowers += 1
                    continue
            if i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[-2] == 0:
                    flowerbed[-1] = 1
                    number_of_new_flowers += 1
                    continue
            if flowerbed[i]==flowerbed[i-1] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                number_of_new_flowers += 1
        return n <= number_of_new_flowers