class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonica deque
        queue = deque()
        start = 0
        ans = []
        for end in range(k):
            while queue and nums[queue[-1]] < nums[end]:
                queue.pop()
            queue.append(end)
        ans.append(nums[queue[0]])

        for end in range(k, len(nums)):
            while queue and queue[0] < end-k+1:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[end]:
                queue.pop()
            queue.append(end)
            ans.append(nums[queue[0]])
        return ans