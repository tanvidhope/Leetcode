class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                template = word[:i]+"_"+word[i+1:]
                graph[template].add(word)
        queue= deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                template = word[:i]+"_"+word[i+1:]
                for neighbour in graph[template]:
                    if neighbour!=word and neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, dist+1))
        return 0