"""
 Disjoint set union implementation with ranks and path compression
 find() have O(log(n)) time complexity in the worst case scenario
 union() have O(log(n)) time complexity in the worst case scenario
"""
class TreeNode:
    '''Linked list object to model disjoint sets as trees'''
    def __init__(self,val,parent = None):
        self.val = val
        self.parent = parent
        self.rank = 0

class DSU:
    '''Disjoint set union data structure'''
    def __init__(self):
        self.dictionary = {}
    def find(self,x):
        '''Finds a node in the forrest, returns an index of the tree'''
        if x not in self.dictionary:
            return None
        tree = self.dictionary[x]
        if not tree.parent:
            return tree.val
        tree.parent = self.dictionary[self.find(tree.parent.val)]
        return tree.parent.val
    def union(self,x,y):
        '''Adds together two trees with given elements'''
        xRoot = self.dictionary[self.find(x)]
        yRoot = self.dictionary[self.find(y)]
        if xRoot.rank > yRoot.rank:
            yRoot.parent = xRoot
        elif xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot
        elif xRoot.val != yRoot.val:
            yRoot.parent = xRoot
            xRoot.rank += 1
    def makeSet(self,x):
        '''Adds a given node to the forrest'''
        self.dictionary[x] = TreeNode(x)
    def addElementToTree(self,x,index):
        '''Adds a given element to a tree with a given index'''
        self.makeSet(x)        
        tree = self.dictionary[x]
        tree.parent = self.dictionary[index] 
    def translateToList(self):
        '''Function returns roots and sets'''
        setdict = {}
        for key in self.dictionary:
            root = self.find(key)
            if root not in setdict:
                setdict[root] = {key}
            else:
                setdict[root].add(key)
        return setdict
    def translateToListWithRanks(self):
        '''Function returns roots and sets'''
        setdict = {}
        for key in self.dictionary:
            root = self.find(key)
            if root not in setdict:
                setdict[root] = [{key},self.dictionary[root].rank]
            else:
                setdict[root][0].add(key)
        return setdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        A = DSU()
        for edge in edges:
            x = A.find(edge[0])
            y = A.find(edge[1])
            if x != None and y != None:
                if x == y:
                    return edge # We found a cycle!
                else:
                    A.union(edge[0],edge[1])
            elif x != None and y == None:
                A.addElementToTree(edge[1],x)
            elif y != None and x == None:
                A.addElementToTree(edge[0],y)
            elif x == None and y == None :
                A.makeSet(edge[0])
                A.makeSet(edge[1])
                A.union(edge[0],edge[1])
        
        
