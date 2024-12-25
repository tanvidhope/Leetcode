class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp
        n = len(arr)
        dp = defaultdict(int)
        answer = 1
        for i in range(n):
            before = dp[arr[i]-difference]
            dp[arr[i]] = before+1
            answer = max(answer, dp[arr[i]])
        return answer