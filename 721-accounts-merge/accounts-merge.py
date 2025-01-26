class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountToName = defaultdict(set)
        graph = defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                accountToName[email] = account[0]
                if email!=account[1]:
                    graph[email].add(account[1])
                    graph[account[1]].add(email)
        visited = set()
        ans = []
        for account in list(accountToName):
            if account not in visited:
                lst = []
                temp = [accountToName[account]]
                self.dfs(graph, account, visited, lst)
                temp.extend(sorted(lst.copy()))
                ans.append(temp)
        return ans

    def dfs(self, graph, account, visited, lst):
        if account not in visited:
            visited.add(account)
            lst.append(account)
            for neighbour in graph[account]:
                self.dfs(graph, neighbour, visited, lst)
        
        