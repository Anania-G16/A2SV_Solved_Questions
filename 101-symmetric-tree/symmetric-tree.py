# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftQueue = deque()
        rightQueue = deque()
        if root.left:
            leftQueue.append(root.left)
        if root.right:
            rightQueue.append(root.right)
        if len(leftQueue) != len(rightQueue):
            return False

        while leftQueue and rightQueue:
            sizeLeft = len(leftQueue)
            sizeRight = len(rightQueue)
            leftArray = []
            rightArray = []
            for i in range(sizeLeft):
                temp = leftQueue.popleft()
                leftArray.append(temp.val)
                if temp.val == 101:
                    continue
                if temp.left:
                    leftQueue.append(temp.left)
                else:
                    leftQueue.append(TreeNode(101))

                if temp.right:
                    leftQueue.append(temp.right)
                else:
                    leftQueue.append(TreeNode(101))

            for i in range(sizeRight):
                temp = rightQueue.popleft()
                rightArray.append(temp.val)
                if temp.val == 101:
                    continue
                if temp.left:
                    rightQueue.append(temp.left)
                else:
                    rightQueue.append(TreeNode(101))
                if temp.right:
                    rightQueue.append(temp.right)
                else:
                    rightQueue.append(TreeNode(101))
            rightArray.reverse()
            if leftArray != rightArray:
                return False
        return True
            


        