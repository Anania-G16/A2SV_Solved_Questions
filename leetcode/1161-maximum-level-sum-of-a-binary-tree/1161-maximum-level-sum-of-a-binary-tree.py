# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxSum = float('-inf')
        result = -1
        level = 1
        while queue:
            size = len(queue)
            running_sum = 0
            for i in range(size):
                temp = queue.popleft()
                running_sum += temp.val
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if running_sum > maxSum:
                result = level
                maxSum = running_sum
            level += 1 

        return result
