class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    transpose.append([])
                transpose[j].append(matrix[i][j])
        return transpose
            