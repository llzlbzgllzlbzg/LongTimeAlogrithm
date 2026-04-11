# 也可以用二叉搜索树的中序遍历是否为升序来判断
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def check(node: Optional[TreeNode], min_val: Optional[int], max_val: Optional[int]) -> bool:
            if node is None:
                return True
            if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
                return False
            return check(node.left, min_val, node.val) and check(node.right, node.val, max_val)
        return check(root, None, None)