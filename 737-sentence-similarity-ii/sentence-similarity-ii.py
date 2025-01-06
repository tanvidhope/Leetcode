
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        graph = defaultdict(set)
        for pair in similarPairs:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])
        
        for i,word in enumerate(sentence1):
            if not self.dfs(word, graph, sentence2[i], set()):
                return False
        return True

    def dfs(self, source, graph, destination, visited):
        if destination == source:
            return True
        for neighbour in graph[source]:
            if neighbour not in visited:
                visited.add(neighbour)
                if self.dfs(neighbour, graph, destination, visited):
                    return True
        return False
