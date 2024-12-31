class RangeModule:

    def __init__(self):
        self.trackingArray = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.trackingArray, left)
        end = bisect.bisect_right(self.trackingArray, right)
        subtrack = []
        if start%2 == 0:   # if start is even, we can say it is outside the current tracking range
            subtrack.append(left)
        if end%2 == 0:
            subtrack.append(right)
        self.trackingArray[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.trackingArray, left)
        end = bisect.bisect_left(self.trackingArray, right)
        return start==end and start%2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.trackingArray, left)
        end=  bisect.bisect_right(self.trackingArray, right)
        subtrack = []
        if start%2 == 1: # if start is odd, we know it is inside an already tracked range
            subtrack.append(left)
        if end%2 == 1:
            subtrack.append(right)
        self.trackingArray[start:end] = subtrack


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)