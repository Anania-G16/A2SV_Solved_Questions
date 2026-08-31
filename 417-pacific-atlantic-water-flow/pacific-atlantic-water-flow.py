class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        directions = [(-1, 0),(1, 0),(0, 1),(0, -1)]
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                pacific = False
                atlantic = False
                visited = set([(row, col)])
                h = heights[row][col]
                queue = deque([(row, col)])
                while queue:
                    size = len(queue)
                    for i in range(size):
                        i, j = queue.popleft()
                        for x, y in directions:
                            newRow = i + x
                            newCol = j + y
                            newDir = (newRow, newCol)
                            if newRow < 0 or newCol < 0:
                                pacific = True
                            elif newRow > len(heights)-1 or newCol > len(heights[0])-1:
                                atlantic = True
                            else:
                                if heights[newRow][newCol] <= heights[i][j] and newDir not in visited:
                                    visited.add(newDir)
                                    queue.append(newDir)
                if pacific and atlantic:
                    result.append([row, col])
        return result



