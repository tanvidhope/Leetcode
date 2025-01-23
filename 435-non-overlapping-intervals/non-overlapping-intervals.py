class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by ending time
        intervals.sort(key=lambda x:x[1])
        remove = 0
        lastFinish = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<lastFinish:
                remove +=1
            else:
                lastFinish = intervals[i][1]
        return remove
