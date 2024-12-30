class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack, store char and count as well
        stack = []
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1]+=1
                if stack[-1][1]>=k:
                    stack.pop()
            else:
                stack.append([i,1])
        string = ""
        for arr in stack:
            string+=(arr[0]*arr[1])
        return string

            

