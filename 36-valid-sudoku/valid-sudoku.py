class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rowsMap = defaultdict(set)
        colsMap = defaultdict(set)
        subMatrices = defaultdict(set)
        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    startRow, startCol = i//3*3, j//3*3
                    if board[i][j] in rowsMap[i] or board[i][j] in colsMap[j] or board[i][j] in subMatrices[(startRow, startCol)]:
                        return False
                    rowsMap[i].add(board[i][j])
                    colsMap[j].add(board[i][j])
                    subMatrices[(startRow, startCol)].add(board[i][j])
        return True       
