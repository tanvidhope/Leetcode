class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxSoFar = 0
        numChunks = 0
        for i, num in enumerate(arr):
            if num > maxSoFar:
                maxSoFar = num
            if i == maxSoFar:
                numChunks+=1
        return numChunks