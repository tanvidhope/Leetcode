class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        for row in board+list(zip(*board)):
            for w in [word, word[::-1]]:
                for s in ''.join(row).split('#'):
                    if len(s)== len(word) and all(s[i] == w[i] or s[i] == ' ' for i in range(len(word))):
                        return True
        return False