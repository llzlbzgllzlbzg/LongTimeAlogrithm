from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(node: Optional['TreeNode']) -> Optional['TreeNode']:
            if node is None:
                return None
            if node == p or node == q:
                return node
            left = check(node.left)
            right = check(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        ans = check(root)
        if ans is None:
            return TreeNode(0)
        return ans