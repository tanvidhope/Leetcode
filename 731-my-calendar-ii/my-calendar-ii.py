class MyCalendarTwo:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.diff[startTime] = self.diff.get(startTime, 0)+1
        self.diff[endTime] = self.diff.get(endTime, 0)-1
        maxCount=  0
        currCount= 0
        for val in self.diff.values():
            currCount += val
            if currCount > 2:
                # rollback changes
                self.diff[startTime]-=1
                self.diff[endTime]+=1
                if self.diff[startTime] == 0:
                    del self.diff[startTime]
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)