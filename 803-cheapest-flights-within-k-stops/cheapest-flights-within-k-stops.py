class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra - priority on cost and number of stops both
        visited = {}
        graph = defaultdict(set)
        for to, fro, price in flights:
            graph[to].add((fro, price))
        pq = [(0, 0, src)]
        while pq:
            cost, stops, node = heapq.heappop(pq)
            if node == dst and stops -1<=k:
                return cost
            if node not in visited or visited[node]>stops:
                visited[node] = stops
                for neighbour, price in graph[node]:
                    heapq.heappush(pq, (cost+price, stops+1, neighbour))
        return -1