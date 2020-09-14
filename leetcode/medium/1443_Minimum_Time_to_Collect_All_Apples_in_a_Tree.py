class GraphNode:
     def __init__(self, val=0, connections = set()):
         self.val = val
         self.connections = connections
         self.apple = False
def CreateTree(n, edges, hasApple):
    dict_nodes = {i: GraphNode(i,set()) for i in range(n)}
    for edge in edges:
        vert1 = edge[0]
        vert2 = edge[1]
        dict_nodes[vert1].connections.add(dict_nodes[vert2])
        dict_nodes[vert2].connections.add(dict_nodes[vert1])
    for i in range(n):
        dict_nodes[i].apple = hasApple[i]
    return dict_nodes[0]
class Solution:
    def minTimeTree(self, root):
        if not root:
            return 0
        result = 0
        while root.connections:
            vertex = root.connections.pop()
            # We eliminate this connection between vertex and root
            vertex.connections.remove(root)
            subgraph = self.minTimeTree(vertex)
            if subgraph != 0 or vertex.apple:
                result += subgraph + 2
        return result
    def minTime(self, n, edges, hasApple):
        root = CreateTree(n, edges, hasApple)
        return self.minTimeTree(root)
