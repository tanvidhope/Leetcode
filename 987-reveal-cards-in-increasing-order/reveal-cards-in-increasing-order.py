class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        queue = deque()
        for i in range(n):
            queue.append(i)
        deck.sort()

        ans = [0]*n
        for card in deck:
            ans[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return ans