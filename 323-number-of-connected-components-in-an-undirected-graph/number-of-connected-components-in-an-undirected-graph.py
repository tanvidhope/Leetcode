class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                self.dfs(i, visited, graph)
                count+=1
        return count
    
    def dfs(self, i, visited, graph):
        for neighbour in graph[i]:
            if neighbour not in visited:
                visited.add(neighbour)
                self.dfs(neighbour, visited, graph)
    