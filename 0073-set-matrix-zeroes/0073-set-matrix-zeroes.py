class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix[0]), len(matrix)
        
        def erase_row_and_col(x,y):

            for r in range(m):
                if matrix[r][y]: matrix[r][y] = "*"
            for c in range(n):
                if matrix[x][c]: matrix[x][c] = "*"

        
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    erase_row_and_col(i,j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0

        return matrix 