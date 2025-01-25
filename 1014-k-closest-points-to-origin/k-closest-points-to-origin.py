class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x,y in points:
            heapq.heappush(pq, (-x*x-y*y, x, y))
            if len(pq)>k:
                heapq.heappop(pq)
        ans = []
        while pq:
            dist, x, y = heapq.heappop(pq)
            ans.append([x, y])
        return ans[::-1]