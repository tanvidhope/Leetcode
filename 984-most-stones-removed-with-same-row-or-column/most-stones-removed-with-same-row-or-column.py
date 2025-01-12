class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph =defaultdict(set)
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].add(j)
                    graph[j].add(i)
        
        numComponents = 0
        visited = set()
        for i in graph:
            if i not in visited:
                visited.add(i)
                self.dfs(graph, i, visited)
                numComponents+=1
        return len(graph) - numComponents

    def dfs(self, graph, node, visited):
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                self.dfs(graph, neighbour, visited)