class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        startDeque = deque()
        resultDeque = deque()
        for i in range(len(start)):
            if start[i] != 'X':
                startDeque.append(i)
        for i in range(len(result)):
            if result[i] != 'X':
                resultDeque.append(i)
        if len(startDeque)!=len(resultDeque):
            return False
        
        while startDeque and resultDeque:
            if start[startDeque[0]] == 'L':
                if result[resultDeque[0]] == 'R' or resultDeque[0] > startDeque[0]:
                    return False
            else:
                if result[resultDeque[0]] == 'L' or resultDeque[0] < startDeque[0]:
                    return False
            startDeque.popleft()
            resultDeque.popleft()
        return True
            