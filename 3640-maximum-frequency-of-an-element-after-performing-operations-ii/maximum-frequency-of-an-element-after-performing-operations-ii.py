class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = Counter(nums)
        sweepLine=defaultdict(int)
        points = set()
        for num in nums:
            sweepLine[num-k]+=1
            sweepLine[num+k+1]-=1
            points.update({num, num-k, num+k+1})
        res = cumulativeSum = 0
        for point in sorted(points):
            cumulativeSum += sweepLine[point]
            res = max(res, freq[point] + min(numOperations, cumulativeSum - freq[point]))
        return res