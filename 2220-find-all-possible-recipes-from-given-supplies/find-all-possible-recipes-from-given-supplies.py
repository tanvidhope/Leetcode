class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # topological sort
        graph = defaultdict(set)
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[recipe].add(ingredient)
        
        queue = deque()
        for supply in supplies:
            queue.append(supply)
        
        ans = set()
        while queue:
            supply = queue.popleft()
            for node in graph:
                if supply in graph[node]:
                    graph[node].remove(supply)
                    if len(graph[node]) == 0:
                        queue.append(node)
                        ans.add(node)
        return list(ans)
        