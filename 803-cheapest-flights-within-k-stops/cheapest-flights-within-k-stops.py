class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for to, fro, price in flights:
            graph[to].add((fro, price))
        queue = deque()
        queue.append((src, 0))
        costs = [float('inf')]*n
        while queue and k>=0:
            m = len(queue)
            for i in range(m):
                curr, cost = queue.popleft()
                for node, price in graph[curr]:
                    if cost+price < costs[node]:
                        costs[node] = cost+ price
                        queue.append((node, costs[node]))
            k-=1
        return costs[dst] if costs[dst]!=float('inf') else -1
