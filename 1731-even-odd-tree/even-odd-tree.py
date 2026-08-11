# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        index = 0
        while queue:
            size = len(queue)
            prev = 0
            for i in range(size):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                if index % 2 == 0:
                    if temp.val % 2 == 0:
                        return False
                    if i == 0:
                        prev = temp.val
                        continue
                    if prev >= temp.val:
                        return False
                    prev = temp.val
                    
                else:
                    if temp.val % 2 == 1:
                        return False
                    if i == 0:
                        prev = temp.val
                        continue
                    if prev <= temp.val:
                        return False
                    prev = temp.val
            index += 1
        return True