class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for x, y, time in meetings:
            graph[x].append((time,y))
            graph[y].append((time,x))
        
        earliest = [inf]*n # earliest time at which a person learned the secret
        earliest[0] = 0
        earliest[firstPerson]  =0
        queue = deque()
        queue.append((0,0))
        queue.append((firstPerson, 0))
        while(len(queue) > 0):
            person, time = queue.popleft()
            for t, nextPerson in graph[person]:
                if t>= time and earliest[nextPerson] > t:
                    earliest[nextPerson] = t
                    queue.append((nextPerson,t))
        return [i for i in range(n) if earliest[i] != inf]
