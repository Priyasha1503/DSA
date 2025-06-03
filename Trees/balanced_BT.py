#https://leetcode.com/problems/balanced-binary-tree/?envType=problem-list-v2&envId=tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        flag=0
        def helper(root):
            if root is None:
                return 0
            l=helper(root.left)
            r=helper(root.right)
            if abs(l-r)>1: return -1
            if l==-1 or r==-1: return -1
            return max(l,r)+1
        y=helper(root)
        if y==-1:
            return False
        else:
            return True
        
