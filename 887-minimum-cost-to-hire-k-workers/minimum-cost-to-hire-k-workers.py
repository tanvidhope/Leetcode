class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # The trick is to realiaze we need to keep the workers with the 
        # lowest wages to quality ratio as it leads to lowest cost
        n = len(quality)
        total_cost = float("inf")
        current_total_quality = 0
        wage_to_quality_ratio = []

        # calculate wage to quality ratio for each worker
        for i in range(n):
            wage_to_quality_ratio.append((wage[i]/quality[i], quality[i]))
        
        # sort workers based on their wage to quality ratio
        wage_to_quality_ratio.sort(key = lambda x:x[0])

        highest_quality_workers = []
        # heap to keep track of highest quality workers
        for i in range(n):
            heapq.heappush(highest_quality_workers, -wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]
            if len(highest_quality_workers) > k:
                current_total_quality += heapq.heappop(highest_quality_workers)
            if len(highest_quality_workers) == k:
                total_cost = min(total_cost, current_total_quality*wage_to_quality_ratio[i][0])
        return total_cost

