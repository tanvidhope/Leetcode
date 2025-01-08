class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # dijkstra
        dist = [float('inf')]*n
        ways = [0]*n
        ways[0] = 1
        dist[0] = 0
        graph = defaultdict(set)
        for road in roads:
            graph[road[0]].add((road[1], road[2]))
            graph[road[1]].add((road[0], road[2]))
        
        pq = []
        pq.append((0,0))
        minCount = 1
        while pq:
            d, node = heapq.heappop(pq)
            for v, time in graph[node]:
                if dist[v] > d+time:
                    dist[v] = d + time
                    ways[v] = ways[node]
                    heapq.heappush(pq, (d+time, v))
                elif dist[v] == d+time:
                    ways[v] = (ways[v]+ways[node])%(10**9+7)

        return ways[n-1]