# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        queue = deque([root])
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if low <= temp.val <= high:
                    result += temp.val
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return result
        
                