class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        currStart, currEnd = nums[0], nums[0]
        ans = []
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if currStart == currEnd:
                    ans.append(str(currEnd))
                else:
                    ans.append(str(currStart) + "->"+str(currEnd))
                currStart = currEnd = nums[i]
            currEnd = nums[i]
        if currStart == currEnd:
            ans.append(str(currEnd))
        else:
            ans.append(str(currStart) + "->"+str(currEnd))
        return ans