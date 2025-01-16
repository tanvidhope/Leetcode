class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph 
        def dfs(start, target):
            if start == target:
                return 1.0
            for neighbour, val in graph[start]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    temp = dfs(neighbour, target)
                    if temp != -1.0:
                        return val*temp
            return -1.0

        graph = defaultdict(set)
        for i, [a,b] in enumerate(equations):
            graph[a].add((b,values[i]))
            graph[b].add((a, 1/values[i]))
        
        ans = []
        for query in queries:
            if query[0] not in graph or query[1] not in graph:
                ans.append(-1.0)
                continue
            visited = set()
            visited.add(query[0])
            ans.append(dfs(query[0], query[1]))
        return ans
