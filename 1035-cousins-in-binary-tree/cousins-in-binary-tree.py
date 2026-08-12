# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        myMap = dict({root.val: 0})
        while queue:
            size = len(queue)
            if x in myMap and y in myMap:
                if myMap[x] != myMap[y]:
                    return True
                else:
                    return False
            for i in range(size):
                temp = queue.popleft()
                del(myMap[temp.val])
                if temp.left:
                    queue.append(temp.left)
                    myMap[temp.left.val] = temp.val
                if temp.right:
                    queue.append(temp.right)
                    myMap[temp.right.val] = temp.val
        return False