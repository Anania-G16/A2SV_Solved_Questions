# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        queue = deque([(root, root.val)])
        while queue:
            size = len(queue)
            for i in range(size):
                temp, running_sum = queue.popleft()
                if running_sum == targetSum and (not temp.left and not temp.right):
                    return True
                if temp.left:
                    queue.append((temp.left, running_sum + temp.left.val))
                if temp.right:
                    queue.append((temp.right, running_sum + temp.right.val))
        return False
