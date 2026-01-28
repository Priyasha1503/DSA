
#https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(p):   # p is root here (root=p)
            if p is None:
                return None
            p.left,p.right=p.right,p.left
            helper(p.left)
            helper(p.right)
            return root
        
        return helper(root)
