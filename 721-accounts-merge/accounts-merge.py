class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        map = {}
        graph = defaultdict(set)
        visited = set()
        for account in accounts:
            for i in range(1, len(account)):
                map[account[i]] = account[0]
                if i>1:
                    graph[account[i]].add(account[1])
                    graph[account[1]].add(account[i])
        ans = []
        for key in map:
            if key not in visited:
                visited.add(key)
                lst = self.dfs(key, visited, graph, [])
                temp = [key]+lst.copy()
                temp.sort()
                ans.append([map[key]]+temp)
        return ans

    def dfs(self, key, visited, graph, lst):
        for neighbour in graph[key]:
            if neighbour not in visited:
                visited.add(neighbour)
                lst.append(neighbour)
                lst = self.dfs(neighbour, visited, graph, lst)
        return lst
