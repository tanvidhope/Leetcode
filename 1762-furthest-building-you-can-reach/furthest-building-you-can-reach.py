class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        i, n = 0, len(heights)
        while (i<(n-1) and ladders > 0):
            if (heights[i+1] - heights[i]) > 0:
                heapq.heappush(pq, heights[i+1]-heights[i])
                ladders-=1
            i+=1
        
        while (i<(n-1) and bricks >= 0):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if pq and pq[0] < diff:
                    bricks-=heapq.heappop(pq)
                    heapq.heappush(pq, diff)
                else:
                    bricks-=diff
            i+=1
        return i if bricks >=0 else i-1

            