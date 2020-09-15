# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def findPath(pathList):
            n = len(pathList[0]) # Length od path to the deepest leave
            m = len(pathList) # Number od deepest leaves
            result = ''
            for i in range(n):
                list_of_choices = []
                for j in range(m):
                    #print(pathList,i,j,list_of_choices,'result',result)
                    if list_of_choices and pathList[j][i] not in list_of_choices:
                        return result # 'L' and 'R' at the same position
                    else:
                        list_of_choices.append(pathList[j][i])
                letter = list_of_choices.pop()
                #print('current result:',result,'new letter:',letter)
                result += letter
            return result
                
        def findRoot(root,path):
            if not path:
                return root
            if path[0] == 'L':
                return findRoot(root.left,path[1:])
            elif path[0] == 'R':
                return findRoot(root.right,path[1:])
            
        
        
        # Step 1 - we find all deepest leaves and remember paths to them
        
        pathList = ['']
        nodeList = [root]
        while True:
            deeperNodeList = []
            deeperPathList = []
            for i in range(len(nodeList)):
                if nodeList[i].left:
                    deeperNodeList.append(nodeList[i].left)
                    deeperPathList.append(pathList[i] + 'L')
                if nodeList[i].right:
                    deeperNodeList.append(nodeList[i].right)
                    deeperPathList.append(pathList[i] + 'R')
            # Lists update
            if not deeperNodeList:
                break
            else:
                # Lists update
                nodeList = deeperNodeList
                pathList = deeperPathList
                #print('List of paths',pathList)
                
        # Step 2 - we have nodeList and pathList of all deepest leaves
        #print(pathList)
        pathToResult = findPath(pathList)
        #print(pathToResult)
        
        # Step 3 - we go to a root using a given path
        
        return findRoot(root,pathToResult)
            
            
                    
                
                    