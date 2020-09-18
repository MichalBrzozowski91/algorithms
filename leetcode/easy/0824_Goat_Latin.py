class Solution:
    def wordTransform(self,word):
        vowels = set(('a','e','i','o','u'))
        if word[0].lower() in vowels:
            return word + 'ma'
        else:
            return word[1:] + word[0] + 'ma'
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        for i in range(len(words)):
            words[i] = self.wordTransform(words[i]) + 'a'*(i+1)
        return ' '.join(words)
    