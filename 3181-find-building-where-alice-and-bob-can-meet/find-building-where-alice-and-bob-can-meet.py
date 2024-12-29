class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # using heaps
        ans= [-1]*len(queries)
        groups = defaultdict(list)
        for i,query in enumerate(queries):
            left,right = sorted(query)
            if left==right or heights[right]>heights[left]:
                ans[i] = right
            else:
                h = max(heights[left], heights[right])
                groups[right].append((h, i))
        minHeap = []
        for i, h in enumerate(heights):
            for queryH, queryI in groups[i]:
                heapq.heappush(minHeap, (queryH, queryI))
            while minHeap and h > minHeap[0][0]:
                queryH, queryI = heapq.heappop(minHeap)
                ans[queryI] = i
        return ans