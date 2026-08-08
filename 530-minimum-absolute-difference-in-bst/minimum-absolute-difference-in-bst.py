# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        minDiff = float('inf')
        values = []
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                values.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        values.sort()
        for i in range(len(values)-1):
            minDiff = min(abs(values[i] - values[i+1]), minDiff)

        return minDiff


            
