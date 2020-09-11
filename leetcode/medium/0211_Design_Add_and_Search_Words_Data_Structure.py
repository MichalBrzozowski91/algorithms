class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if str(len(word)) in self.elements:
            self.elements[str(len(word))].add(word)
        else:
            self.elements[str(len(word))] = {word}
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        #print(self.elements)
        if str(len(word)) not in self.elements:
            return False
        for element in self.elements[str(len(word))]:
            word_check = True
            for i in range(len(element)):
                if word[i] != '.' and word[i] != element[i]:
                    word_check = False
                    break # Word does not match
                else:
                    continue
            if word_check:
                return True # This is the word
            else:
                continue
        return False
                    
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
