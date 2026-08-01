class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        freshCount = 0
        minutes = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        while queue and freshCount:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for x, y in directions:
                    nr = r + x
                    nc = c + y
                    if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) :
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            freshCount -= 1
                            queue.append((nr, nc))
            minutes += 1
        if freshCount > 0:
            return -1
        return minutes
