class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = dict()
        child = dict()
        rootCount = 0
        root = -1
        multiParentCount = 0
        for i in range(n):
            parent[i] = []
            child[i] = []
        for i in range(n):
            if leftChild[i] != -1:
                parent[leftChild[i]].append(i)
                child[i].append(leftChild[i])
            if rightChild[i] != -1:
                parent[rightChild[i]].append(i)
                child[i].append(rightChild[i])





        for key, value in parent.items():
            if value == []:
                rootCount += 1
                root = key
            elif len(value) > 1:
                multiParentCount += 1
        if rootCount != 1 or multiParentCount != 0:
            return False
        
        queue = deque([root])
        visited = set()
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if temp in visited:
                    return False
                visited.add(temp)
                count += 1
                for node in child[temp]:
                    queue.append(node)
        return count == n
                

        
        