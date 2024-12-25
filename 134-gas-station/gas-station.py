class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGain, currGain, answer = 0, 0,0 
        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            totalGain+=gas[i]-cost[i]
            currGain +=gas[i]-cost[i]

            if currGain<0:
                currGain = 0
                answer = i+1
        return answer if totalGain>=0 else -1