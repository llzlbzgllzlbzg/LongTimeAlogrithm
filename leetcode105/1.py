from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None or inorder is None:
            return None
        hashmap = {}
        for index, value in enumerate(inorder):
            hashmap[value] = index
        def build(preorder_left: int, inorder_left: int, length: int) -> Optional[TreeNode]:
            root = TreeNode(preorder[preorder_left])
            index = hashmap[root.val]
            left_length = index - inorder_left
            right_length = length - left_length - 1
            if left_length > 0:
                root.left = build(preorder_left + 1, index - left_length, left_length)
            if right_length > 0:
                root.right = build(preorder_left + left_length + 1, index + 1, right_length)
            return root
        return build(0, 0, len(preorder))