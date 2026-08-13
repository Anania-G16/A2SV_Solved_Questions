# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque([cloned])
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if temp.val == target.val:
                    return temp
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        