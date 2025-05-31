#https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        #LEFT - ROOT - RIGHT
        def helper(root,lst):
            if root is None:
                return lst
            else:
                helper(root.left,lst)
                lst.append(root.val)
                helper(root.right,lst)
            return lst
        return helper(root,[])
