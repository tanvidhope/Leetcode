class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        else:
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        par1 = self.find(x)
        par2 = self.find(y)
        if par1 == par2:
            return False
        self.parent[par1] = par2
        return True
    
    def isParentSame(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()
        for equation in equations:
            if equation[1] == "=":
                dsu.union(equation[0], equation[3])
        for equation in equations:
            if equation[1] == "!":
                if dsu.isParentSame(equation[0], equation[3]):
                    return False
        return True
        