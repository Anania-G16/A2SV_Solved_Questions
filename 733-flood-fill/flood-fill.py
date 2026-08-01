class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        queue = deque()
        queue.append((sr, sc))
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        if color == original:
            return image
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for x, y in directions:
                nr = r + x
                nc = c + y
                if (nr < len(image) and 0 <= nr) and (nc < len(image[0]) and 0 <= nc):
                    if image[nr][nc] == original:
                        queue.append((nr, nc))
        return image

