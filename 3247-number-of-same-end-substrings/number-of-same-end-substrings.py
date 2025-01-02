class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        # prefix sum to store the count of each letter
        n = len(s)
        charFreqPrefixSum = [[0]*n for i in range(26)]
        # fill the frequency table
        for i,char in enumerate(s):
            charFreqPrefixSum[ord(char) - ord('a')][i]+=1
        
        # make it prefix sum
        for freq in charFreqPrefixSum:
            for j in range(1,n):
                freq[j]+=freq[j-1]
        
        results = []
        for left, right in queries:
            count = 0
            #for each character
            for freq in charFreqPrefixSum:
                leftFreq = 0 if left == 0 else freq[left-1]
                rightFreq = freq[right]
                frequencyInRange = rightFreq - leftFreq
                count+=frequencyInRange *(frequencyInRange+1)//2
            results.append(count)
        return results

