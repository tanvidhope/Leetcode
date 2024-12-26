class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
      #graph, dijkstra cos weights
      m, n= len(heights), len(heights[0])
      distances = [[float('inf')]*n for i in range(m)]
      distances[0][0] = 0
      queue = [(0,0, 0)] #(row, col, dist)
      neighbours=  {(0,1), (0, -1), (1, 0), (-1, 0)}
      while queue:
        r, c, dist = queue.pop(0)
        if r==m-1 and c==n-1:
            continue
        for neighbour in neighbours:
            newr, newc = r+neighbour[0], c+neighbour[1]
            if 0<=newr<m and 0<=newc<n and distances[newr][newc]> max(dist, abs(heights[r][c] - heights[newr][newc])):
                distances[newr][newc] = max(dist, abs(heights[r][c] - heights[newr][newc]))
                queue.append((newr, newc, distances[newr][newc]))
      return distances[m-1][n-1]