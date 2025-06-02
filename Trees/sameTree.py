# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        def helper(p,q):
            '''if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False'''
            #instead of 2nd and 3rd ,1st test cases we could write this as weel
            if not p or not q:
                return p==q
            
            if p.val==q.val:
                return helper(p.left,q.left) and helper(p.right,q.right)
            else:
                return False

        return helper(p,q)
