class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []

        for i in range(len(matrix)):
            row_min = min(matrix[i])
            col = matrix[i].index(row_min)

            is_max = True

            for j in range(len(matrix)):
                if matrix[j][col] > row_min:
                    is_max = False
                    break

            if is_max:
                result.append(row_min)

        return result