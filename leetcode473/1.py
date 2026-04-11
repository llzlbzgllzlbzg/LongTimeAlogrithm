from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        res = self._rootSum(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res
    
    def _rootSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        res = 1 if root.val == targetSum else 0
        res += self._rootSum(root.left, targetSum - root.val)
        res += self._rootSum(root.right, targetSum - root.val)
        return res