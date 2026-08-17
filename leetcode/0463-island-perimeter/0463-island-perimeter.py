class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0)])
        visited = set([(0,0)])
        perimeter = 0
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        while queue:
            size = len(queue)
            for i in range(size):
                a, b = queue.popleft()
                for x, y in directions:
                    newDirection = (a+x, b+y)
                    if 0 <= newDirection[0] < len(grid) and 0 <= newDirection[1] < len(grid[0]):
                        if newDirection not in visited:
                            visited.add(newDirection)
                            queue.append(newDirection)
                        if grid[a][b] == 1:
                            if grid[a+x][b+y] == 0:
                                perimeter += 1
                    else:
                        if grid[a][b] == 1:
                            perimeter += 1
        return perimeter
            