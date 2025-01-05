class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        matches = {} # key = girl, value = boy
        
        def dfs(boy, visited):
            # match this boy with a potential match
            # go through all girls and fine one that maximises ans

            for girl in range(n):
                # rule 1- only ask the girl if you haven't asked her before
                # rule 2 - if the girl is already taken, she'll only go with you if her partner finds a new match
                if grid[boy][girl] == 1 and girl not in visited:
                    visited.add(girl)
                    if girl not in matches or dfs(matches[girl], visited):
                        matches[girl] = boy
                        return True
            return False
        
        for boy in range(m):
            dfs(boy, set())
            
        return len(matches)
