class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # O(n2) TC
        def dfs(u,v):
            if u==v:
                return True
            for neighbour in graph[u]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour, v):
                        return True
            return False

        graph = defaultdict(set)
        for u,v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)