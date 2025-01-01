class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums)-k+1):
            subarray = nums[i:i+k]
            freq = Counter(subarray)
            pq = []
            for key in freq:
                heapq.heappush(pq, (-freq[key], -key))
            sum = 0
            for _ in range(x):
                if pq:
                    fr, node = heapq.heappop(pq)
                    sum+=(-node*-fr)
            ans.append(sum)
        return ans