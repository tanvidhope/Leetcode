class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # dijkstra
        m,n =len(heights), len(heights[0])
        pq = []
        dist = [[float('inf')]*n for i in range(m)]
        pq.append((0,0,0))
        while pq:
            wt, i, j = heapq.heappop(pq)
            if i==m-1 and j==n-1:
                return wt
            directions = {(i+1, j), (i, j+1), (i-1, j), (i, j-1)}
            for newi, newj in directions:
                if 0<=newi<m and 0<=newj<n and dist[newi][newj] > max(wt,abs(heights[i][j] - heights[newi][newj])):
                    dist[newi][newj] = max(wt,abs(heights[i][j] - heights[newi][newj]))
                    heapq.heappush(pq,(max(wt,abs(heights[i][j] - heights[newi][newj])), newi, newj))
        return -1