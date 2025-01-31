class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k>=len(cardPoints) :
            return sum(cardPoints)
        currSum = sum(cardPoints[:k])
        maxSum = currSum
        n = len(cardPoints)
        for i in range(k):
            currSum-= cardPoints[k-1-i]
            currSum += cardPoints[n-1-i]
            maxSum = max(maxSum, currSum)
        return maxSum
