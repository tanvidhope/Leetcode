class Solution:

    def __init__(self, w: List[int]):
        self.weights = w.copy()
        self.n = len(w)
        self.sum = sum(w)

    def pickIndex(self) -> int:
        target = self.sum * random.random()
        prefixSum = 0
        for i in range(self.n):
            prefixSum+=self.weights[i]
            if target<prefixSum:
                return i
            



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()