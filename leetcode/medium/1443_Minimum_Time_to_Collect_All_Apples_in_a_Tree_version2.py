class Solution:
    def helper(self, vertex, connections, hasApple):
        result = 0
        while connections[vertex]:
            vertex2 = connections[vertex].pop()
            connections[vertex2].remove(vertex)
            subgraph = self.helper(vertex2, connections, hasApple)
            if subgraph != 0 or hasApple[vertex2]:
                result += 2 + subgraph
        return result
        
    def minTime(self, n, edges, hasApple):
        # Create a list of connections
        connections = [set() for _ in range(n)]
        for edge in edges:
            connections[edge[0]].add(edge[1])
            connections[edge[1]].add(edge[0])
        return self.helper(0,connections, hasApple)
