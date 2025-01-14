class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or timestamp < self.map[key][0][0]:
            return ""
        lst = self.map[key]
        index = 0
        left, right = 0, len(lst)
        while left<right:
            mid = left+(right-left)//2
            if lst[mid][0] <= timestamp:
                left = mid+1
            else:
                right = mid
        return "" if right == 0 else lst[right-1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)