class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}
        return self.findProbability(n, k, row, column, memo)

    def findProbability(self, n, k, row, col, memo):
        if k==0 and 0<=row<n and 0<=col<n:
            return 1
        if k<=0 or row<0 or col<0 or row>=n or col>=n:
            return 0
        if (k, row, col) not in memo:
            probs = 0
            neighbours = {(2,1), (2, -1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)}
            for neighbour in neighbours:
                newi, newj = row+neighbour[0], col+neighbour[1]
                probs += 0.125*self.findProbability(n, k-1, newi, newj, memo)
            memo[(k, row, col)] = probs
        return memo[(k, row, col)]