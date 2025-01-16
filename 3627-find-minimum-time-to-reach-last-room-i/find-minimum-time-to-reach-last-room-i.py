class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # dijkstra
        pq = []
        pq.append((0, 0, 0)) # time, i, j
        m, n = len(moveTime), len(moveTime[0])
        seen = set()
        seen.add((0,0))
        while pq:
            currTime, i,j = heapq.heappop(pq)
            if i==m-1 and j==n-1:
                return currTime
            neighbours = {(i, j+1), (i+1, j), (i-1, j), (i, j-1)}
            for newi, newj in neighbours:
                if 0<=newi<m and 0<=newj<n and (newi, newj) not in seen:
                    heapq.heappush(pq, (max(moveTime[newi][newj], currTime)+1, newi, newj))
                    seen.add((newi, newj))
        return currTime
            