class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # sweepline
        edges = []
        for i, building in enumerate(buildings):
            edges.append((building[0], i))
            edges.append((building[1], i))
        
        edges.sort()
        live, ans = [], []
        idx = 0
        while idx<len(edges):
            currX = edges[idx][0]
            # handling all edges at a given x
            while idx < len(edges) and edges[idx][0] == currX:
                buildingIndex = edges[idx][1]
                # if its a left edge
                if buildings[buildingIndex][0] == currX:
                    # add to priorityqueue
                    height, right = buildings[buildingIndex][2], buildings[buildingIndex][1]
                    heapq.heappush(live, [-height, right])
                # if tallest builginf ends, pop it
                while live and live[0][1]<=currX:
                    heapq.heappop(live)
                idx+=1
            maxHeight = -live[0][0] if live else 0

            if not ans or maxHeight != ans[-1][-1]:
                ans.append([currX, maxHeight])
        return ans
