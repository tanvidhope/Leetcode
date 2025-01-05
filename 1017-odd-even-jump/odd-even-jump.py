class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nextHigher, nextLower = [0]*n, [0]*n
        stack = []
        for num, i in sorted([num,i] for i,num in enumerate(arr)):
            while stack and stack[-1] < i:
                nextHigher[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for num, i in sorted([-num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                nextLower[stack.pop()] = i
            stack.append(i)
        
        higher, lower = [0]*n, [0]*n
        higher[-1] = lower[-1] = 1
        for i in range(n-1)[::-1]:
            higher[i] = lower[nextHigher[i]]
            lower[i] = higher[nextLower[i]]
        return sum(higher)