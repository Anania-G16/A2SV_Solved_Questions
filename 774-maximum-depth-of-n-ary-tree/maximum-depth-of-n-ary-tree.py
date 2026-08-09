"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                temp = queue.popleft()
                for node in temp.children:
                    queue.append(node)
        return depth
