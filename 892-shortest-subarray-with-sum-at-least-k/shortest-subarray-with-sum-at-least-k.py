class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # priority queue
        n = len(nums)
        shortestLength = float('inf')
        cumulativeSum = 0
        prefixSumHeap = []
        for i,num in enumerate(nums):
            cumulativeSum+=num
            if cumulativeSum >= k:
                shortestLength = min(shortestLength, i+1)
            while prefixSumHeap and cumulativeSum - prefixSumHeap[0][0] >=k:
                shortestLength = min(shortestLength, i-heapq.heappop(prefixSumHeap)[1])
            heappush(prefixSumHeap, (cumulativeSum, i))
        return -1 if shortestLength == float('inf') else shortestLength