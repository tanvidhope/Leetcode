class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                template = word[:i]+"_"+word[i+1:]
                graph[template].add(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                template = word[:i]+"_"+word[i+1:]
                for neighbour in graph[template]:
                    if neighbour != word and neighbour not in visited:
                        queue.append([neighbour, steps+1])
                        visited.add(neighbour)
        return 0
            