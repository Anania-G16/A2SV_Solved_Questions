# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque([root])
        result = []
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
            result.append(array)
        result.reverse()
        return result


