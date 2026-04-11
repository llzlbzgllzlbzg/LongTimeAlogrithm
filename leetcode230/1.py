from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        self.k = k
        self.result = -1
        self._inorder(root)
        return self.result
    
    def _inorder(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return
        self._inorder(node.left)
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self._inorder(node.right)