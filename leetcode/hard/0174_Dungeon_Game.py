class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # In the outcome grid we will obtain the initial health for each subproblem
        m = len(dungeon) # Number of rows
        n = len(dungeon[0]) # Number of columns
        if m == 0 or n == 0:
            return 0
        # Princess square
        dungeon[m-1][n-1] = max(1,1 - dungeon[m-1][n-1]) # The knight must have at least 1 health to survive a final demon encounter
        #print(dungeon)
        # Last row
        for j in range(n - 2, -1,-1):
            current_place = dungeon[m-1][j]
            optimal_path = dungeon[m-1][j+1] # We move to the right
            dungeon[m-1][j] = max(optimal_path - current_place,1)
            #print(dungeon)
        for i in range(m - 2, -1,-1):
            # Last column
            current_place = dungeon[i][n-1]
            optimal_path = dungeon[i+1][n-1] # We move down
            dungeon[i][n-1] = max(optimal_path - current_place,1)
            #print(dungeon)
            for j in range(n-2, -1,-1):
                current_place = dungeon[i][j]
                optimal_path = min(dungeon[i+1][j],dungeon[i][j+1]) # We choose an optimal direction
                dungeon[i][j] = max(optimal_path - current_place,1)
                #print(dungeon)
        return dungeon[0][0]
