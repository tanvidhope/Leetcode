class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        for i, task in enumerate(tasks):
            order.append([task[0], task[1], i])
        order.sort(key=lambda x:x[0])

        heap = []
        currTime = 0
        i = 0
        n = len(order)
        ans = []
        while i<n or heap:
            if not heap and i<n and order[i][0] > currTime:
                currTime = order[i][0]
            while i<n and order[i][0] <= currTime:
                heapq.heappush(heap, (order[i][1], order[i][2]))
                i+=1
            if heap:
                time, task = heapq.heappop(heap)
                currTime+=time
                ans.append(task)
        return ans
            