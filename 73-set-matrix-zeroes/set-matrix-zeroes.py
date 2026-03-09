class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        columns = []
        for i in range (len(matrix)):
            if 0 in matrix[i]:
                row.append(i)
                column = [j for j,n in enumerate(matrix[i]) if n == 0]
                columns += column
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row:
                    matrix[i][j] = 0
                if j in columns:
                    matrix[i][j] = 0




        