class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(9)]
        cols = [set() for j in range(9)]
        subMatrix = defaultdict(set)
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    startRow, startCol = (i//3)*3, (j//3)*3
                    subMatrix[(startRow, startCol)].add(num)
                else:
                    emptyCells.append((i,j))
        ans = self.recurse(board, emptyCells, 0, rows, cols, subMatrix)
        return ans

    def recurse(self, board, emptyCells, curr, rows, cols, subMatrix):
        if curr>=len(emptyCells):
            return board
        for x in range(1,10):
            if self.canPlace(x,board,emptyCells[curr][0], emptyCells[curr][1], rows, cols, subMatrix):
                i,j = emptyCells[curr][0], emptyCells[curr][1]
                board[i][j] = str(x)
                rows[i].add(x)
                cols[j].add(x)
                subMatrix[((i//3)*3, (j//3)*3)].add(x)
                ans = self.recurse(board, emptyCells, curr+1, rows, cols, subMatrix)
                if ans != []:
                    return ans
                board[i][j] = "."
                rows[i].remove(x)
                cols[j].remove(x)
                subMatrix[((i//3)*3, (j//3)*3)].remove(x)
        return []
        
    def canPlace(self,num, board, i,j, rows, cols,subMatrix):
        startRow, startCol = (i//3)*3 , (j//3)*3
        if num not in rows[i] and num not in cols[j] and num not in subMatrix[(startRow, startCol)]:
            return True
        return False