# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque([root])
        result = []
        reverse = False
        while queue:
            size = len(queue)
            array = []
            for i in range(size):
                temp = queue.popleft()
                array.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if reverse:
                array.reverse()
            reverse = not reverse
            result.append(array)
        return result
