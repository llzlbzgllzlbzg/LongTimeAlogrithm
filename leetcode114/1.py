from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        dummy = TreeNode(0, None, root)
        self.current = dummy
        self._preorder(root)

    def _preorder(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return
        left = node.left
        right = node.right
        node.left = None
        self.current.right = node
        self.current = node
        self._preorder(left)
        self._preorder(right)