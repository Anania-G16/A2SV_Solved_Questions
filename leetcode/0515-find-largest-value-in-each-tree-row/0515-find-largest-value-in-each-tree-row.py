# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            maxNum = float('-inf')
            for i in range(size):
                temp = queue.popleft()
                maxNum = max(maxNum, temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            result.append(maxNum)
        return result
