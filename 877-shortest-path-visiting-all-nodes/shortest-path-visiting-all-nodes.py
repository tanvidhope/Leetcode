class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        n = len(graph)
        endingMask  = (1<<n) -1
        queue = [(node, 1<<node) for node in range(n)]
        seen = set(queue)
        steps = 0

        while queue:
            nextQueue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbour in graph[node]:
                    # visit the neighbour, by setting the mask
                    nextMask = mask | (1 << neighbour)
                    if nextMask == endingMask:
                        return 1+steps
                    if (neighbour, nextMask) not in seen:
                        seen.add((neighbour, nextMask))
                        nextQueue.append((neighbour, nextMask))
            steps+=1
            queue = nextQueue