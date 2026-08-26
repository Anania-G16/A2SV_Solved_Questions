class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        result = []
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        for start, destination in queries:
            queue = deque([(start, 1.0)])
            gotcha = False
            visited = set([start])
            if start not in graph:
                result.append(-1.0)
                continue
            while queue:
                size = len(queue)
                for i in range(size):
                    node, running_product = queue.popleft()
                    if node == destination:
                        result.append(running_product)
                        gotcha = True
                        break
                    for i in range(len(graph[node])):
                        eq, cost = graph[node][i]
                        if eq not in visited:
                            queue.append((eq, running_product*cost))
                            visited.add(eq)
            if not gotcha:
                result.append(-1.0) 
        return result  

                    
            