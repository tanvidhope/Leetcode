class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        #sweepline
        records = []
        maxPos = 0
        for i,[start, end] in enumerate(paint):
            records.append((start, i, 1))
            records.append((end, i, -1))
            maxPos = max(maxPos, end)
        
        records.sort()
        ans = [0 for i in range(len(paint))]
        indexes = []
        endedSet = set()
        i = 0
        for pos in range(maxPos+1):
            while i<len(records) and records[i][0] == pos:
                pos, index, type = records[i]
                if type == 1:
                    heapq.heappush(indexes, index)
                else:
                    endedSet.add(index)
                i+=1
            while indexes and indexes[0] in endedSet:
                heapq.heappop(indexes)
            if indexes:
                ans[indexes[0]]+=1
        return ans