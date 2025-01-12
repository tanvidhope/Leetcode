class DSU:
    def __init__(self, n):
        self.parent= [i for i in range(n+1)]
        self.n = n
    
    def find(self, u):
        if self.parent[u]!= u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        par1 = self.find(u)
        par2 = self.find(v)
        if par1 == par2:
            return False
        self.parent[par2] = par1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DSU
        dsu = DSU(1000)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        return []
