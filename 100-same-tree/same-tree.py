# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
     
        def traversal(nodeP, nodeQ):
            if not nodeP and not nodeQ:
                return True
            if not nodeP or not nodeQ:
                return False
            if nodeP.val != nodeQ.val:
                return False
           

            result = traversal(nodeP.left, nodeQ.left)
            if not result:
                return False

            result = traversal(nodeP.right, nodeQ.right)
            if not result:
                return False
            return True

        result = traversal(p, q)
        return result
