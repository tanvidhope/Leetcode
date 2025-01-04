class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # cooldown queue
        freq = Counter(tasks)
        pq = []
        for key in freq:
            heapq.heappush(pq, (-freq[key], key))
        intervals = 0
        cooldown = deque()
        while pq or cooldown:
            while cooldown and cooldown[0][0] < intervals:
                _, task, freq = cooldown.popleft()
                heapq.heappush(pq, (freq, task))
            if pq:
                freq, task = heapq.heappop(pq)
                if freq < -1:
                    cooldown.append((intervals+n, task, freq+1))
            intervals+=1
        return intervals
