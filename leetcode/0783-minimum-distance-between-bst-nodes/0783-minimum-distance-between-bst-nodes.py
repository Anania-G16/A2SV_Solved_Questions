class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.minDiff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.minDiff = min(
                    self.minDiff,
                    node.val - self.prev
                )

            self.prev = node.val

            inorder(node.right)

        inorder(root)

        return self.minDiff