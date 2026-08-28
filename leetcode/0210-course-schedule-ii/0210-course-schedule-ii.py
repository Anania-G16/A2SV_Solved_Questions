class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisite = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        queue = deque()

        for c, p in prerequisites:
            prerequisite[c] += 1
            graph[p].append(c)
        
        for key, value in prerequisite.items():
            if value == 0:
                queue.append(key)
        if len(queue) == 0:
            return []
        result = []
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                result.append(temp)
                for node in graph[temp]:
                    prerequisite[node] -= 1
                    if prerequisite[node] == 0:
                        queue.append(node)
                       
        if len(result) == numCourses:
            return result
        else:
            return []