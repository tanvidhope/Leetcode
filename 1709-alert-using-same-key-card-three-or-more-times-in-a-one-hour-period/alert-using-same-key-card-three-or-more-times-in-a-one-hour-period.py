class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hmap = defaultdict(deque)
        pairs = []
        for i in range(len(keyName)):
            time = self.convert(keyTime[i])
            pairs.append((keyName[i], time))
        pairs.sort(key=lambda x: x[1])
        ans = set()
        for person, time in pairs:
            hmap[person].append(time)
            while hmap[person][0] < time-100:
                hmap[person].popleft()
            if len(hmap[person])>=3:
                ans.add(person)
        return sorted(list(ans))
    
    def convert(self,keyTime):
        time = 0
        for i in range(5):
            if keyTime[i] == ":":
                continue
            time = time*10+int(keyTime[i])
        return time