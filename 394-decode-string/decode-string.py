class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                string = ""
                while stack and stack[-1]!= "[":
                    string+=stack.pop()
                num = ""
                stack.pop()
                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                count = int(num[::-1])
                stack.append(string*count)
            else:
                stack.append(char)
        ans = ""
        while stack:
            ans+=stack.pop()
        return ans[::-1]