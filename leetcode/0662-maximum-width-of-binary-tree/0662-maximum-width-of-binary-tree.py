# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        index = 0
        maxWidth = 0
        queue = deque([(root, index)])
        x=0
        leftMostIndex = 0
        rightMostIndex = 0
        while queue:
            size = len(queue)
            for i in range(size):
                temp, index = queue.popleft()
                if i == 0:
                    leftMostIndex = index
                if i == size-1:
                    rightMostIndex = index
                if temp.left:
                    queue.append((temp.left, 2*index + 1))
                if temp.right:
                    queue.append((temp.right, 2*index + 2))
            maxWidth = max(maxWidth, rightMostIndex - leftMostIndex + 1)
        return maxWidth
