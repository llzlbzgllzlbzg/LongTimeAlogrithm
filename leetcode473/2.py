from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(lambda: 0)
        prefix[0] += 1
        def check(root: Optional[TreeNode], currSum: int) -> int:
            if root is None:
                return 0
            currSum += root.val
            res = prefix[currSum - targetSum]
            prefix[currSum] += 1
            res += check(root.left, currSum)
            res += check(root.right, currSum)
            prefix[currSum] -= 1
            return res
        return check(root, 0)