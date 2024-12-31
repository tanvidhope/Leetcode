class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # relative order of L and R must remain unchanged
        # have a queue to keep track of order
        startDeque, targetDeque = deque(), deque()
        for i in range(len(target)):
            if start[i]!="_":
                startDeque.append(i)
            if target[i]!="_":
                targetDeque.append(i)
        
        if len(startDeque)!=len(targetDeque):
            return False
        while startDeque and targetDeque:
            if start[startDeque[0]]=="L":
                if targetDeque[0] > startDeque[0] or target[targetDeque[0]] == "R":
                    return False
            elif start[startDeque[0]] == "R":
                if targetDeque[0] < startDeque[0] or target[targetDeque[0]] == "L":
                    return False
            startDeque.popleft()
            targetDeque.popleft()
        return True