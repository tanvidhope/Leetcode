"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        #priority queue
        pq = []
        shiftStart = float('inf')
        for i,person in enumerate(schedule):
            heapq.heappush(pq, (person[0].start, person[0].end, i, 0))
            shiftStart = min(shiftStart, person[0].start)
        ans = []
        commonEndTime = 0
        while pq:
            startTime, endTime, person, index = heapq.heappop(pq)
            commonEndTime = max(commonEndTime, endTime)
            if index+1< len(schedule[person]):
                nextInterval = schedule[person][index+1]
                heapq.heappush(pq, (nextInterval.start, nextInterval.end, person, index+1))
            if pq and pq[0][0] > commonEndTime:
                ans.append(Interval(commonEndTime, pq[0][0]))
        return ans
        