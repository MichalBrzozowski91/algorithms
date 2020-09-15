class Solution:
    # O(n) hashmap solution
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Refactored - changing connections in-place
        dictionaryEdges = {i: [] for i in range(n)}
        for con in connections:
            dictionaryEdges[con[0]].append([con[1],1]) # 1 - forward; 0 - backward
            dictionaryEdges[con[1]].append([con[0],0])
        #print(dictionaryEdges)
          
        # Dfs from root 0:
        currentLevel = [0]
        nextLevel =[]
        counter = 0
        while currentLevel:
            for node in currentLevel:
                while dictionaryEdges[node]:
                    con = dictionaryEdges[node][0]
                    dictionaryEdges[node].remove([con[0],con[1]])
                    dictionaryEdges[con[0]].remove([node,1-con[1]])
                    nextLevel.append(con[0])
                    if con[1] == 1:
                        counter += 1
            currentLevel = nextLevel
            nextLevel = []
        return counter