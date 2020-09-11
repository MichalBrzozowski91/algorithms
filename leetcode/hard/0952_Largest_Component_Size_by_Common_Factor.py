# List of primes from 1 to 20000

import math

# A function to print all prime factors of  
# a given number n 
def prime_factors(n): 
    result = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        result.append(2), 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i and divide n 
        while n % i== 0: 
            result.append(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        result.append(n)
    return result

# Euclidian algorithm

def euclid(a,b):
    #print(a,b)
    a,b = min(a,b), max(a,b)
    if a == 1:
        return a
    if a == 0:
        return b
    return euclid(a,b % a)

class TreeNode:
    '''Linked list object to model disjoint sets as trees'''
    def __init__(self,val,parent = None):
        self.val = val
        self.parent = parent
        self.rank = 0
        self.amount = 0

# Disjoint set union data structure

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
            xRoot.amount += yRoot.amount
        elif xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot
            yRoot.amount += xRoot.amount
        elif xRoot.val != yRoot.val:
            yRoot.parent = xRoot
            xRoot.rank += 1
            xRoot.amount += yRoot.amount
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
    def increment(self,x):
        index = self.find(x)
        self.dictionary[index].amount += 1
    def amounts(self):
        '''Function returns roots and sets'''
        setdict = {}
        for key in self.dictionary:
            root = self.find(key)
            if root not in setdict:
                setdict[root] = self.dictionary[root].amount
        return setdict








class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if A == [1]:
            return 1
        forrest = DSU()
        for i in range(len(A)):
            if A[i] == 1:
                continue
            primes = prime_factors(A[i])
            found = None
            for p in primes:
                index = forrest.find(p)
                if not index:
                    forrest.makeSet(p)
                    if found:
                        forrest.union(p, found)
                    found = p
                else:
                    if found:
                        forrest.union(found, p)
                    else:
                        found = p
            forrest.increment(found)
            #print(A[i],forrest.translateToList())
            #print(A[i],forrest.amounts())
        #print(forrest.translateToList())
        #print(forrest.amounts())
        amounts = forrest.amounts()
        result = 0
        for key in amounts:
            result = max(result,amounts[key])
        return result
        
