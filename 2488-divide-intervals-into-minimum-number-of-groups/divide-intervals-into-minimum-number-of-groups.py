class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # kinda like graph colouring
        pq = []
        intervals.sort()
        for interval in intervals:
            if pq and pq[0] < interval[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, interval[1])
        return len(pq)