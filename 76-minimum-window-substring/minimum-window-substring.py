class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqTarget = Counter(t)
        distinctNeeded = len(freqTarget)
        freq = defaultdict(int)
        start, end = 0, 0
        minStart, minEnd = 0,len(s)+1
        while end<len(s):
            freq[s[end]]+=1
            if s[end] in freqTarget and freq[s[end]] == freqTarget[s[end]]:
                distinctNeeded-=1

            while distinctNeeded==0:
                if (end-start+1) < (minEnd-minStart+1):
                    minStart, minEnd = start, end
                freq[s[start]]-=1
                if freq[s[start]] < freqTarget[s[start]]:
                    distinctNeeded+=1
                start+=1
            end+=1
        return s[minStart:minEnd+1] if minEnd != len(s)+1 else ""
