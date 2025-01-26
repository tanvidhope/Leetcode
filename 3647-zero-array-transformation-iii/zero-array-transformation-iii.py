class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        chosen = []
        queries.sort()
        candidates = []
        n = len(nums)
        j, ans = 0, 0
        for i in range(n):
            while j<len(queries) and queries[j][0] == i:
                # we prioritize the range query with the furthest ending point
                heapq.heappush(candidates, -queries[j][1])
                j+=1
            nums[i] -= len(chosen)
            while nums[i] > 0 and candidates and -candidates[0]>=i:
                ans+=1
                #chosen needs to keep track of which queries have ended and remove them
                # hence the minHeap
                heapq.heappush(chosen, -heapq.heappop(candidates))
                nums[i]-=1
            if nums[i] >0:
                return -1
            while chosen and chosen[0] <=i:
                heapq.heappop(chosen)
        return len(queries) - ans
            


