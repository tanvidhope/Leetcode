class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        # dijkstra/ MST
        # We have to find a common point (LCA) of the 2 paths, from where the paths converge into 1 to reach dest
        # Can do with running dijkstra 3 times - first for finding the dist from src1 to all other nodes
        # 2nd ffor finding the dist from src2 to all other nodes
        # 3 for finding the dist from destination to all other nodes.
        # for the 3rd dijkstra, we need a reversed graph (reverse adjacency list), since the edges need to be reversed
        # And now, consider each node in the graph as the LCA and find the sum of dist of src1 src2 and dest from that node
        # the min sum of the distances of src1 src3 and dest to a node is our ans

        graph = defaultdict(set)
        reversedGraph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add((edge[1], edge[2]))
            reversedGraph[edge[1]].add((edge[0], edge[2]))
        
        arr1 = self.dijkstra(src1, graph, n)
        arr2 = self.dijkstra(src2, graph, n)
        arr3 = self.dijkstra(dest, reversedGraph, n)

        ans = float('inf')
        for i in range(n):
            ans = min(ans, arr1[i]+arr2[i]+arr3[i])
        return ans if ans < float('inf') else -1

    def dijkstra(self, source, graph, n):
        distances = [float('inf')]*n
        distances[source] = 0
        pq = []
        pq.append((0, source))
        while pq:
            dist, node = heapq.heappop(pq)
            for neighbour in graph[node]:
                if dist + neighbour[1] < distances[neighbour[0]]:
                    distances[neighbour[0]] = dist+neighbour[1]
                    heapq.heappush(pq, (distances[neighbour[0]], neighbour[0]))
        return distances

