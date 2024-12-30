class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(int)
        for start in range(len(s)):
            character = s[start]
            substringLength = 0
            for end in range(start, len(s)):
                if character == s[end]:
                    substringLength+=1
                    count[(character, substringLength)] +=1
                else:
                    break
        ans = -1
        for i in count:
            length = i[1]
            if count[i] >= 3 and length > ans:
                ans = length
        return ans