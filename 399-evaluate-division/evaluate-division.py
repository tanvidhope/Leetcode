class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        for i in range(n):
            equation = equations[i]
            graph[equation[0]].append([equation[1], values[i]])
            graph[equation[1]].append([equation[0], 1/values[i]])
        ans = []
        for query in queries:
            ans.append(self.bfs(query, graph))

        return  ans

    def bfs(self, query, graph):
        start, dest = query[0], query[1]
        if start not in graph or dest not in graph:
            return -1.0
        queue = deque()
        visited =set()
        queue.append([start, 1])
        while (len(queue) > 0):
            [node, value] = queue.popleft()
            if node == dest:
                return value
            for neighbour in graph[node]:
                if neighbour[0] not in visited:
                    visited.add(neighbour[0])
                    queue.append([neighbour[0], neighbour[1]*value])
        return -1.0
                