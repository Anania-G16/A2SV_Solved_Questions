# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth = 1
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if not temp.left and not temp.right:
                    return depth
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            depth += 1
        return 0
