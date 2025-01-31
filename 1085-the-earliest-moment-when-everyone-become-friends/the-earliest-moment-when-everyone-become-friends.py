class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        par1 = self.find(x)
        par2 = self.find(y)
        if par1==par2:
            return False
        self.parents[par1] = par2
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        dsu = DSU(n)
        clusters = n
        logs.sort()
        for i, [time, a, b] in enumerate(logs):
            if dsu.union(a,b):
                clusters-=1
            else:
                if clusters == 1:
                    return logs[i-1][0]
        return -1 if clusters > 1 else logs[-1][0]