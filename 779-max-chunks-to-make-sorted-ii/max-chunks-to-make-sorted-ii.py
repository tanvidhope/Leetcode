class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        #prefix max and suffixMinarray
        # if max of left subarray < min of the right subarray -> always can chunck out
        n = len(arr)
        prefixMax = [0]*n
        suffixMin = [0]*n
        prefixMax[0], suffixMin[n-1] = arr[0], arr[n-1]
        for i in range(1,n):
            prefixMax[i] = max(prefixMax[i-1], arr[i])
            suffixMin[n-i-1] = min(suffixMin[n-i], arr[n-i-1])

        numChunks = 1
        for i in range(n):
            if prefixMax[i-1] <= suffixMin[i]:
                numChunks+=1
        return min(numChunks, n)