class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.maxScore = 0
        letterMap = defaultdict(int)
        freq = [0 for i in range(26)]
        subsetLetters = [0 for i in range(26)]
        for letter in letters:
            freq[ord(letter) - ord('a')] +=1

        self.check(len(words)-1, words, score, subsetLetters, 0, freq)
        return self.maxScore

    def check(self,i, words, score, subsetLetters, totalScore, freq):

        def isValidWord(subsetLetters, freq):
            for c in range(26):
                if freq[c] < subsetLetters[c]:
                    return False
            return True

        if i == -1:
            self.maxScore = max(self.maxScore, totalScore)
            return
        n = len(words[i])
        for char in words[i]:
            c = ord(char) - ord('a')
            subsetLetters[c]+=1
            totalScore+=score[c]
        if isValidWord(subsetLetters, freq):
            self.check(i-1, words, score, subsetLetters, totalScore, freq)
        for char in words[i]:
            c = ord(char) - ord('a')
            subsetLetters[c]-=1
            totalScore-=score[c]
        self.check(i-1, words, score, subsetLetters, totalScore, freq)
    
                
