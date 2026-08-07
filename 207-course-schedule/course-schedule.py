class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = []
        indegree = dict()
        processed = 0
        queue = deque()
        graph = [[] for i in range(numCourses)]
        for i in range(numCourses):
            indegree[i] = 0
        
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        for node, value in indegree.items():
            if value == 0:
                queue.append(node)

        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                processed += 1
                for node in graph[temp]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        queue.append(node)
        return processed == numCourses