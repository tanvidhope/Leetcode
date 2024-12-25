class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i>=0 and j<n:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j+=1
            else:
                i-=1
        return False