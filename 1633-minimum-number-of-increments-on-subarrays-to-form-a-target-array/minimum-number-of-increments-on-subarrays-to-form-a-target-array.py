class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # do a reverse of difference array
        # convert array to difference array
        n = len(target)
        differenceArr = [0]*(n)
        differenceArr[0] = target[0]
        for i in range(1, n):
            differenceArr[i] = target[i] - target[i-1]

        # now count all positive number in the difference array
        count = 0
        for element in differenceArr:
            if element > 0:
                count+=element
        return count  