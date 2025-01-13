class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # keep mono stack, remove letter in stack if its greater than current letter and
        # there is another occurence of the letter later on
        lastOccurence = {c:i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and stack[-1] > s[i] and i<lastOccurence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(s[i])
                seen.add(s[i])
        return ''.join(stack)