# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        while current:
            if p.val > current.val and q.val > current.val:
                    current = current.right
                # If both p and q are lesser than parent, LCA is in left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # We found the split point, which is the LCA
            else:
                return current
        