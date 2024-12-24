class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i, j = 0, 0
        count = 0
        minElement, maxElement = deque(), deque()
        for j, num in enumerate(nums):
            while maxElement and nums[maxElement[-1]] < num:
                maxElement.pop()
            maxElement.append(j)
            while minElement and nums[minElement[-1]] > num:
                minElement.pop()
            minElement.append(j)
            
            while maxElement and nums[maxElement[0]]-nums[minElement[0]] > 2:
                if maxElement[0] < minElement[0]:
                    i = maxElement[0]+1
                    maxElement.popleft()
                else:
                    i = minElement[0]+1
                    minElement.popleft()
            count+=j-i+1
        return count
