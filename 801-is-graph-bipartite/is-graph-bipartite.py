class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        for i in range(len(graph)):
            if i not in visited and not self.partition(graph, i, 0, visited):
                return False
        return True
        
    def partition(self, graph, node, color, visited):
        if node in visited:
            return False if visited[node] !=color else True
        visited[node] = color
        for neighbour in graph[node]:
            if not self.partition(graph, neighbour, 1-color, visited):
                return False
        return True