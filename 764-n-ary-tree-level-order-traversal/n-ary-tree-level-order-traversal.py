"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            array = []
            for i in range(size):
                temp = queue.popleft()
                array.append(temp.val)
                for child in temp.children:
                    queue.append(child)
            result.append(array)
        return result
        