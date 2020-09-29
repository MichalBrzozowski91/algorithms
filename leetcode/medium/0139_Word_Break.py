class TreeNode:
    def __init__(self, val = '', children = {}, word_end = False):
        self.val = val
        self.children = children
        self.word_end = word_end

class Solution:
    def search(self,s, root):
        node = root
        for letter in s:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        return True
        
        
    def wordBreak(self, s, wordDict):
        # Creating a trie
        trie = TreeNode()
        for word in wordDict:
            node = trie
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TreeNode(letter,{})
                    node = node.children[letter]
                else:
                    node = node.children[letter]
            node.word_end = True
        # Create a set of words
        wordSet = set(wordDict)
        candidates = {''}
        for letter in s:
            new_candidates = set()
            for candidate in candidates:
                candidate += letter
                if candidate in wordSet:
                    new_candidates.add('')
                if self.search(candidate,trie):
                    new_candidates.add(candidate)
            candidates = new_candidates
            if not candidates:
                return False
        if '' in candidates:
            return True
        else:
            return False
