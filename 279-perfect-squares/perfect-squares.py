class Solution:
    def numSquares(self, n: int) -> int:
        i = 1
        arr = []
        perfects = []
        while i*i <= n:
            perfects.append(i*i)
            arr.append((i*i, i*i))
            i += 1
        queue = deque(arr)
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for i in range(size):
                perfect, running_sum = queue.popleft()
                if running_sum == n:
                    return level
                if running_sum > n:
                    continue
                i = 0
                while i < len(perfects) and perfects[i] <= perfect:
                    queue.append((perfects[i], running_sum + perfects[i]))
                    i += 1
        return 0
