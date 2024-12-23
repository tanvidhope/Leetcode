class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        candidates = []
        chosen = []
        ans, n, j = 0, len(nums), 0
        for i in range(n):
            while j<len(queries) and queries[j][0] == i:
                heapq.heappush(candidates, -queries[j][1])
                j+=1
            nums[i]-=len(chosen)
            while nums[i] > 0 and candidates and -candidates[0] >=i:
                ans+=1
                heapq.heappush(chosen, -heapq.heappop(candidates))
                nums[i]-=1
            if nums[i]>0:
                return -1
            while chosen and chosen[0] <= i:
                heapq.heappop(chosen)
        return len(queries) - ans

            