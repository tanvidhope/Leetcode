class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        stack = []
        arr = [0]*n
        for i in range(n):
            if s[i]=='(':
                stack.append(i)
                continue
            if stack and s[stack[-1]]=='(':
                open =stack.pop()
                arr[i] = 1
                arr[open] = 1
        for i in range(1, n):
            arr[i] = arr[i-1]+arr[i] if arr[i] != 0 else 0
        return max(arr)