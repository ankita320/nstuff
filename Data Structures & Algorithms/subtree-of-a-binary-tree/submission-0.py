# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases
        if not subRoot: 
            return True  # An empty tree is always a subtree
        if not root: 
            return False # A non-empty subRoot cannot be a subtree of an empty root
        
        # If the trees are identical starting at the current node, return True
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, check if subRoot exists in the left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # If both nodes are null, they are identical
        if not p and not q:
            return True
        
        # If only one node is null, or values don't match, they aren't identical
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check both left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        