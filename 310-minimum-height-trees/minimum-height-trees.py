class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        adj_list = defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

            degree[a] += 1
            degree[b] += 1

        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = len(degree)
        
        while remaining > 2:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for neighbor in adj_list[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
            remaining -= size
        result = []
        for node in queue:
            result.append(node)
        return result
