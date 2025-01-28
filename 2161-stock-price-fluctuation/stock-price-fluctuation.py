class StockPrice:

    def __init__(self):
        self.latestTime = 0
        #store price of stock at each timestamp
        self.timestampPriceMap = {}
        # store stock prices in increasing order to get max and min
        self.priceFrequency = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        self.latestTime = max(self.latestTime, timestamp)
        if timestamp in self.timestampPriceMap:
            oldPrice = self.timestampPriceMap[timestamp]
            self.priceFrequency[oldPrice]-=1
            if self.priceFrequency[oldPrice] == 0:
                del self.priceFrequency[oldPrice]
        
        # add latest price
        self.timestampPriceMap[timestamp] = price
        if price in self.priceFrequency:
            self.priceFrequency[price]+=1
        else:
            self.priceFrequency[price] = 1

    def current(self) -> int:
        return self.timestampPriceMap[self.latestTime]

    def maximum(self) -> int:
        return self.priceFrequency.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.priceFrequency.peekitem(0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()