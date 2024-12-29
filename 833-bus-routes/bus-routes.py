class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        graph = defaultdict(set)
        for i in range(len(routes)):
            routes[i].sort()
        self.createGraph(routes, graph)
        queue = deque()
        self.addStartingNodes(queue, routes, source)
        visited = set()
        busCount = 1
        while queue:
            size = len(queue)
            while size>0:
                size-=1
                node = queue.popleft()
                if self.isStopExist(routes[node], target):
                    return busCount
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            busCount+=1
        return -1

    def createGraph(self, routes, graph):
        for i in range(len(routes)):
            for j in range(i+1, len(routes)):
                if self.haveCommonNode(routes[i], routes[j]):
                    graph[i].add(j)
                    graph[j].add(i)

    def haveCommonNode(self, route1, route2):
        i,j = 0, 0
        while (i<len(route1) and j<len(route2)):
            if route1[i] == route2[j]:
                return True
            if route1[i]<route2[j]:
                i+=1
            else:
                j+=1
        return False  

    def addStartingNodes(self, queue, routes, source):
        for i in range(len(routes)):
            if self.isStopExist(routes[i], source):
                queue.append(i)
    
    def isStopExist(self, route, stop):
        for j in range(len(route)):
            if route[j] == stop:
                return True
        return False