class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        par1 = self.find(x)
        par2 = self.find(y)
        if par1==par2:
            return False
        self.parent[par1] = par2
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        dsu = DSU(n)
        for edge in edges:
            if dsu.union(edge[0], edge[1]):
                components-=1
        return components