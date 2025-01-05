class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickup = []
        drop = []
        for trip in trips:
            pickup.append([trip[1], trip[0]])
            drop.append([trip[2], trip[0]])
        pickup.sort()
        drop.sort()
        i, j = 0, 0
        n = len(trips)
        currPassengers=0
        while (i<n and j<n):
            if pickup[i][0] < drop[j][0]:
                currPassengers+=pickup[i][1]
                i+=1
                if currPassengers > capacity:
                    return False
            else:
                currPassengers-=drop[j][1]
                j+=1
        return True