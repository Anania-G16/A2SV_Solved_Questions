class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mleft, mright = 0, len(matrix)-1
        n = len(matrix[0])-1
        while mleft <= mright:
            mid = (mleft + mright) // 2
            if target < matrix[mid][0] :
                mright = mid - 1
            elif target > matrix[mid][n]:
                mleft = mid + 1
            else:
                left, right = 0, n
                while left <= right:
                    middle = (left + right) // 2
                    if target < matrix[mid][middle]:
                        right = middle - 1
                    elif target > matrix[mid][middle]:
                        left = middle + 1
                    else:
                        return True
                break
        return False
                