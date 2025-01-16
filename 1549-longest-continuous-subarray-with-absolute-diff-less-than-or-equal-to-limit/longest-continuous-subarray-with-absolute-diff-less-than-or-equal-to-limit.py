class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # max and min deque
        maxDeque = deque()
        minDeque = deque()
        maxLen = 0
        start = 0
        for end in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]]<nums[end]:
                maxDeque.pop()
            maxDeque.append(end)
            while minDeque and nums[minDeque[-1]] > nums[end]:
                minDeque.pop()
            minDeque.append(end)
            if (nums[maxDeque[0]] - nums[minDeque[0]]) <= limit:
                maxLen = max(maxLen, end-start+1)
            else:
                while start < end and (nums[maxDeque[0]] - nums[minDeque[0]]) > limit:
                    if minDeque[0] == start:
                        minDeque.popleft()
                    if maxDeque[0] == start:
                        maxDeque.popleft()
                    start+=1
        return maxLen
