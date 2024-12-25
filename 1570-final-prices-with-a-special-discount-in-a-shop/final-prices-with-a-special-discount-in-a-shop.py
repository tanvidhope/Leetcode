class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # daily temperatures
        stack = []
        ans = prices.copy()
        for i in range(len(prices)-1, -1, -1):
            while stack and prices[stack[-1]]>prices[i]:
                stack.pop()
            if stack:
                ans[i] = prices[i]-prices[stack[-1]]
            else:
                ans[i] = prices[i]
            stack.append(i)
        return ans