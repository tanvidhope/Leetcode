class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq = []
        projects = list(zip(capital, profits))
        projects.sort()
        ptr = 0
        n = len(projects)
        for i in range(k):
            while ptr<n and projects[ptr][0] <=w:
                heapq.heappush(pq, -projects[ptr][1])
                ptr+=1
            if not pq:
                break
            w-=heapq.heappop(pq)
        return w