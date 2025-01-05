class MyCalendarThree:

    def __init__(self):
        self.startTimes = []
        self.endTimes = []

    def book(self, startTime: int, endTime: int) -> int:
        self.startTimes.append(startTime)
        self.endTimes.append(endTime)
        self.startTimes.sort()
        self.endTimes.sort()
        maxBookings, currBookings = 0, 0
        n, i, j = len(self.startTimes), 0, 0
        currEnd = -1
        while i<n:
            if self.startTimes[i] >= self.endTimes[j]:
                currBookings-=1
                j+=1
            else:
                currBookings+=1
                i+=1
                maxBookings = max(maxBookings, currBookings)
        return maxBookings
            


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)