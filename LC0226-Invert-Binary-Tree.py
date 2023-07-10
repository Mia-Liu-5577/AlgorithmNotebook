import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap_nodes(self, node):
        node.left, node.right = node.right, node.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_q = []
        node_q.append(root)
        while len(node_q) > 0:
            node = node_q.pop(0)
            if node:
                self.swap_nodes(node)
                node_q.append(node.left)
                node_q.append(node.right)
        return root

# =====================================

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfsHelper(self, node):
        if node:
            self.dfsHelper(node.left)
            self.dfsHelper(node.right)
            node.left, node.right = node.right, node.left
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.dfsHelper(root)
        return root

# =====================================

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


