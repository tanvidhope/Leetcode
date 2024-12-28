class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [0]*n
        skip = False
        indexInDeck = 0
        indexInAns = 0
        deck.sort()
        while indexInDeck < n:
            if ans[indexInAns] == 0:
                if not skip:
                    ans[indexInAns] = deck[indexInDeck]
                    indexInDeck+=1
                skip = not skip
            indexInAns = (indexInAns+1)%n
        return ans