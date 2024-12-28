class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = [] # stores (-gain, passes, totalStudents)
        for passes, tot in classes:
            gain= self.calculateGain(passes, tot)
            heapq.heappush(maxHeap, (-gain, passes, tot))
        
        for i in range(extraStudents):
            currGain, passes, tot = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-self.calculateGain(passes+1, tot+1), passes+1, tot+1))

        # final avg pass ratio
        totalPassRatio = 0
        while maxHeap:
            _, passes, totalStudents = heapq.heappop(maxHeap)
            totalPassRatio+= passes/totalStudents
        return totalPassRatio/len(classes)

    def calculateGain(self, passes, totalStudents):
        return (passes+1)/(totalStudents+1) - passes/totalStudents