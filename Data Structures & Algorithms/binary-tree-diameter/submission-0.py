# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0
        
        def dfs(node):
            # Base case: an empty node has a height/depth of 0
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # The diameter at the current node is the sum of left and right depths
            current_diameter = left_depth + right_depth
            
            # Update the global maximum diameter found so far
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the depth of the current subtree to the parent node
            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return self.max_diameter