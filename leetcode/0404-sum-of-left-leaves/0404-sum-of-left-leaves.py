# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        total = 0
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                    if not temp.left.left and not temp.left.right:
                        total += temp.left.val
                if temp.right:
                    queue.append(temp.right)
        return total