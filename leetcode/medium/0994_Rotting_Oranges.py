class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh_oranges = set()
        rotten_oranges = set()
        new_rotten_oranges = set()
        empty_squares = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_oranges.add((i,j))
                elif grid[i][j] == 2:
                    rotten_oranges.add((i,j))
        counter = 0
        while fresh_oranges:
            if not rotten_oranges:
                return -1
            counter += 1
            for orange in rotten_oranges:
                if (orange[0]-1,orange[1]) in fresh_oranges:
                    fresh_oranges.remove((orange[0]-1,orange[1]))
                    new_rotten_oranges.add((orange[0]-1,orange[1]))
                if (orange[0] + 1,orange[1]) in fresh_oranges:
                    fresh_oranges.remove((orange[0]+1,orange[1]))
                    new_rotten_oranges.add((orange[0]+1,orange[1]))
                if (orange[0],orange[1]-1) in fresh_oranges:
                    fresh_oranges.remove((orange[0],orange[1]-1))
                    new_rotten_oranges.add((orange[0],orange[1]-1))
                if (orange[0],orange[1]+1) in fresh_oranges:
                    fresh_oranges.remove((orange[0],orange[1]+1))   
                    new_rotten_oranges.add((orange[0],orange[1]+1))
            rotten_oranges = new_rotten_oranges.copy()
            new_rotten_oranges = set()
            #print('counter',counter,'fresh:',fresh_oranges,'\n new_rotten_oranges',rotten_oranges) 
        return counter