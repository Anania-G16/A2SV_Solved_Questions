class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        up = False
        right = True
        steps = 1
        result = [[rStart, cStart]]
        while len(result) < rows*cols:
            for i in range(steps):
                if right:
                    cStart += 1
                else:
                    cStart -= 1
                if (rStart < rows and rStart > -1) and (cStart < cols and cStart > -1):
                    result.append([rStart, cStart])
            right = not right

            for i in range(steps):
                if up:
                    rStart -= 1
                else:
                    rStart += 1
                if (rStart < rows and rStart > -1) and (cStart < cols and cStart > -1):        
                    result.append([rStart, cStart])
            up = not up
            steps += 1
    
        return result