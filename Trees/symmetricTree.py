# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''if root.left and root.right is None:
            return True
        if root.left or root.right is None:
            return False'''
        def helper(p,q):
            '''if root is None:
                return True
            if root.left is None and root.right is None:
                return True
            if root.left is None and root.right is not None:
                return False
            if root.left is not None and root.right is None:
                return False
            p=root.left
            q=root.right
            if p.val==q.val:
                return helper(root.left'''
            if not p or not q:
                return p==q
            
            if p.val==q.val:
                return helper(p.left,q.right) and helper(p.right,q.left)
            else:
                return False
        return helper(root.left,root.right)
                                                     
