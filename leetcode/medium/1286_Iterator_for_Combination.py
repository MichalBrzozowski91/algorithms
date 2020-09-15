class CombinationIterator:
    def translate(self,characters, result_list):
        translated =''
        for number in result_list:
            translated += characters[number]
        return translated

    def __init__(self, characters: str, combinationLength: int):
        
        self.characters = characters
        self.charLength = len(characters)
        self.combinationLength = combinationLength
        if self.charLength  < combinationLength:
            self.nextCombination = None
        else:
            self.nextCombination = list(range(combinationLength))
            self.numbers_set = set(range(combinationLength))
            
    def next(self) -> str:
        if not self.nextCombination:
            raise StopIteration
        A = self.nextCombination
        B = self.nextCombination.copy()
        #print('Current:',A)
        lastElement = list(range(self.charLength - self.combinationLength,self.charLength))
        if A == lastElement:
            self.nextCombination = None
            return self.translate(self.characters,B)
        for i in reversed(range(self.combinationLength)):
            if A[i] != lastElement[i]:
                A[i] += 1
                for j in range(i+1,self.combinationLength):
                    A[j] = A[j-1] + 1
                return self.translate(self.characters,B)
        self.nextCombination = None
        return self.translate(self.characters,B)
    def hasNext(self) -> bool:
        #print(self.nextCombination)
        return self.nextCombination != None


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()