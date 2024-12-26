from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.deque = deque()
        self.sl = SortedList()
        self.total = self.firstK = self.lastK = 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.deque.append(num)
        index = self.sl.bisect_left(num)
        if index < self.k:
            self.firstK += num
            if len(self.sl) >= self.k:
                self.firstK -= self.sl[self.k - 1]
        if index >= len(self.sl) + 1 - self.k:
            self.lastK += num
            if len(self.sl) >= self.k:
                self.lastK -= self.sl[-self.k]
        self.sl.add(num)
        if len(self.deque) > self.m:
            num = self.deque.popleft()
            self.total -= num
            index = self.sl.index(num)
            if index < self.k:
                self.firstK -= num
                self.firstK += self.sl[self.k]
            elif index >= len(self.sl) - self.k:
                self.lastK -= num
                self.lastK += self.sl[-self.k - 1]
            self.sl.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.sl) <self.m:
            return -1
        return (self.total - self.firstK - self.lastK)//(self.m-2*(self.k))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()