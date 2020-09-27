class  GraphNode:
    def __init__(self,val = '',children = [], costs = []):
        self.val = val
        self.children = children
        self.costs = costs
# Graph search
class Solution:
    def createGraph(self,equations,values):
        mapping = {}
        for eq, val in zip(equations, values):
            if eq[0] not in mapping:
                mapping[eq[0]] = GraphNode(eq[0],[eq[1]],[val])
            else:
                mapping[eq[0]].children.append(eq[1])
                mapping[eq[0]].costs.append(val)
            if eq[1] not in mapping:
                mapping[eq[1]] = GraphNode(eq[1],[eq[0]],[1/val])
            else:
                mapping[eq[1]].children.append(eq[0])
                mapping[eq[1]].costs.append(1/val)
            
        return mapping
    def calculateResult(self, mapping, q, seen):
        if q[0] not in mapping or q[1] not in mapping:
            return None
        if q[0] == q[1]:
            return 1.0
        for node, cost in zip(mapping[q[0]].children,mapping[q[0]].costs):
            if node == q[1]:
                return cost
            if node in seen:
                continue
            candidate = self.calculateResult(mapping, [node,q[1]], seen | {q[0]})
            if candidate != None:
                return cost*candidate
        return None
            
            
    def calcEquation(self, equations, values, queries):
        mapping = self.createGraph(equations, values)
        res = []
        for q in queries:
            check = self.calculateResult(mapping, q, set())
            if check == None:
                res.append(-1.0)
            else:
                res.append(check)
        return res
