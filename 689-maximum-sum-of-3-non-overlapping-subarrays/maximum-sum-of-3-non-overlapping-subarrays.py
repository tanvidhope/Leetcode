class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # number of possible subarrays 
        n = len(nums)-k+1

        #precompute the sum of k-length subarrays
        sums= [sum(nums[:k])]
        for i in range(k,len(nums)):
            sums.append(sums[-1]-nums[i-k]+nums[i])
        
        # memo[i][j] = max sum possible startign from index i with j subarrays remaining
        memo = [[-1]*4 for i in range(n)]
        indices = []

        self.dp(sums, k, 0, 3, memo)

        self.dfs(sums, k, 0, 3, memo, indices)

        return indices

    def dp(self, sums, k, index, remaining, memo):
        if remaining == 0:
            return 0
        if index>=len(sums):
            return float('-inf') if remaining > 0 else 0
        if memo[index][remaining] == -1:
            # take current subarray vs skip it
            withCurrent = sums[index]+ self.dp(sums, k, index+k, remaining-1, memo)
            skipCurrent = self.dp(sums, k, index+1, remaining, memo)
            memo[index][remaining]= max(withCurrent, skipCurrent)
        return memo[index][remaining]
    
    def dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums):
            return

        with_current = sums[idx] + self.dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self.dp(sums, k, idx + 1, rem, memo)

        # Choose path that gave optimal result in DP
        if with_current >= skip_current:  # Take current subarray
            indices.append(idx)
            self.dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:  # Skip current subarray
            self.dfs(sums, k, idx + 1, rem, memo, indices)
        