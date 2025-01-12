class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m ,n = len(isWater), len(isWater[0])
        dist = [[float('inf')]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    dist[i][j] = 0
        

        while queue:
            i,j = queue.popleft()
            neighbours = {(i, j+1), (i+1,j), (i, j-1), (i-1, j)}
            for di,dj in neighbours:
                if 0<=di<m and 0<=dj<n and isWater[di][dj] == 0 and dist[di][dj]>dist[i][j]+1:
                    dist[di][dj] = dist[i][j]+1
                    queue.append((di, dj))
        return dist
