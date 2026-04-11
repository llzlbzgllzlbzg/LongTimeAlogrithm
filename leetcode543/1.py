from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.ans = 0
        self._depth(root)
        return self.ans - 1
        
    def _depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left_depth = self._depth(node.left)
        right_depth = self._depth(node.right)
        self.ans = max(self.ans, left_depth + right_depth + 1)
        return max(left_depth, right_depth) + 1