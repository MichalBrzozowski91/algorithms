class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i in range(0,len(asteroids) - 1):
            if asteroids[i] > 0 and asteroids[i+1] < 0: #Collision
                if abs(asteroids[i+1]) > abs(asteroids[i]):
                    del asteroids[i]
                    i = max(i-1,0)
                    continue
                if abs(asteroids[i+1]) < abs(asteroids[i]):
                    del asteroids[i+1]
                    continue
                if abs(asteroids[i+1]) == abs(asteroids[i]):
                    del asteroids[i+1]
                    del asteroids[i]
                    i = max(i-1,0)
                    continue
            else:
                i += 1
        return asteroids
