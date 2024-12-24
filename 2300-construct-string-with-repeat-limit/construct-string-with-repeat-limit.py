class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        pq = []
        for char in freq:
            heapq.heappush(pq, (-ord(char), freq[char]))

        ans = ""
        while pq:
            charNeg, count = heapq.heappop(pq)
            char = chr(-charNeg)
            use = min(repeatLimit, count)
            ans+=char*use
            if count > use and pq:
                nextCharNeg, nextCount = heapq.heappop(pq)
                nextChar = chr(-nextCharNeg)
                ans+=nextChar
                if nextCount > 1:
                    heapq.heappush(pq, (nextCharNeg, nextCount-1))
                heapq.heappush(pq, (charNeg, count - use))
        return ans


            