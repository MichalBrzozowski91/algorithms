class Solution:
    def divisorGame(self, N: int) -> bool:
        #win_Alice = [False]*1001 # Index j is equal to True iff Alice wins when the game starts at the number j
        #win_Alice[1] = False
        #for i in range(2, N+1):
        #    divisors = [x for x in range(1,i) if i % x == 0]
        #    for d in divisors:
        #        if not win_Alice[i - d]:
        #            win_Alice[i] = True
        #return win_Alice[N]
        return N % 2 == 0    